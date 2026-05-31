# from odoo import http


# class QsPurchase(http.Controller):
#     @http.route('/qs_purchase/qs_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qs_purchase/qs_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qs_purchase.listing', {
#             'root': '/qs_purchase/qs_purchase',
#             'objects': http.request.env['qs_purchase.qs_purchase'].search([]),
#         })

#     @http.route('/qs_purchase/qs_purchase/objects/<model("qs_purchase.qs_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qs_purchase.object', {
#             'object': obj
#         })

