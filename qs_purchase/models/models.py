# from odoo import models, fields, api


# class qs_purchase(models.Model):
#     _name = 'qs_purchase.qs_purchase'
#     _description = 'qs_purchase.qs_purchase'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

