# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools import sql


class AsPlanningLine(models.Model):
    _name = 'as.planning.line'
    _description = 'Global Planning Line'
    _auto = False

    name = fields.Char(string='Name', required=True)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_stop = fields.Datetime(string='End Date', required=True)
    record_type = fields.Selection([
        ('po', 'Purchase Order'),
        ('mo', 'Manufacturing Order'),
        ('so', 'Sales Order'),
    ], string='Record Type', required=True)
    res_id = fields.Integer(string='Resource ID', required=True)
    model = fields.Char(string='Model', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner')
    project_id = fields.Many2one('project.project', string='Project')

    def init(self):
        """Initialize the SQL VIEW that aggregates PO, MO, and SO records."""
        sql.drop_view_if_exists(self.env.cr, 'as_planning_line')
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW as_planning_line AS (
                -- Purchase Orders
                SELECT
                    (po.id * 10 + 1)::bigint AS id,
                    po.name || ' - ' || COALESCE(rp.name, '')::text AS name,
                    po.date_approve AS date_start,
                    po.date_planned AS date_stop,
                    'po'::text AS record_type,
                    po.id AS res_id,
                    'purchase.order'::text AS model,
                    po.partner_id AS partner_id,
                    NULL::integer AS project_id
                FROM purchase_order po
                LEFT JOIN res_partner rp ON po.partner_id = rp.id
                WHERE po.date_approve IS NOT NULL
                  AND po.date_planned IS NOT NULL

                UNION ALL

                -- Manufacturing Orders
                SELECT
                    (mp.id * 10 + 2)::bigint AS id,
                    mp.name || ' - ' || COALESCE(rp.name, '')::text AS name,
                    mp.date_start AS date_start,
                    mp.date_deadline AS date_stop,
                    'mo'::text AS record_type,
                    mp.id AS res_id,
                    'mrp.production'::text AS model,
                    NULL::integer AS partner_id,
                    mp.project_id AS project_id
                FROM mrp_production mp
                LEFT JOIN project_project pp ON mp.project_id = pp.id
                LEFT JOIN res_partner rp ON pp.partner_id = rp.id
                WHERE mp.date_start IS NOT NULL
                  AND mp.date_deadline IS NOT NULL
                  AND mp.state NOT IN ('cancel', 'done')

                UNION ALL

                -- Sales Orders
                SELECT
                    (so.id * 10 + 3)::bigint AS id,
                    so.name || ' - ' || COALESCE(rp.name, '')::text AS name,
                    so.commitment_date AS date_start,
                    so.commitment_date::timestamp AS date_stop,
                    'so'::text AS record_type,
                    so.id AS res_id,
                    'sale.order'::text AS model,
                    so.partner_id AS partner_id,
                    NULL::integer AS project_id
                FROM sale_order so
                LEFT JOIN res_partner rp ON so.partner_id = rp.id
                WHERE so.commitment_date IS NOT NULL
                  AND so.state NOT IN ('cancel', 'done')
            )
        """)

    def action_open_source(self):
        """Open the source record that this planning line represents."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': self.model,
            'res_id': self.res_id,
            'view_mode': 'form',
            'target': 'current',
        }