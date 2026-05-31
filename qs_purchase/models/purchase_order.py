from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    manufacturing_id = fields.Many2one(
        'mrp.production',
        string="Manufacturing Order"
    )