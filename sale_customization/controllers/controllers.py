# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCustomization(http.Controller):
#     @http.route('/sale_customization/sale_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_customization/sale_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_customization.listing', {
#             'root': '/sale_customization/sale_customization',
#             'objects': http.request.env['sale_customization.sale_customization'].search([]),
#         })

#     @http.route('/sale_customization/sale_customization/objects/<model("sale_customization.sale_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_customization.object', {
#             'object': obj
#         })
