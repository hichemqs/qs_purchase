from odoo import models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def action_view_purchase_orders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders generated from %s' % self.name,
            'res_model': 'purchase.order',
            'view_mode': 'list,form,gantt',
            'views': [
                (False, 'list'),
                (False, 'form'),
                (False, 'gantt'),
            ],
            'domain': [('origin', '=', self.name)],
        }