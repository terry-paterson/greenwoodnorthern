# -*- coding: utf-8 -*-
# from odoo import http


# class MigrationFixes(http.Controller):
#     @http.route('/migration_fixes/migration_fixes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/migration_fixes/migration_fixes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('migration_fixes.listing', {
#             'root': '/migration_fixes/migration_fixes',
#             'objects': http.request.env['migration_fixes.migration_fixes'].search([]),
#         })

#     @http.route('/migration_fixes/migration_fixes/objects/<model("migration_fixes.migration_fixes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('migration_fixes.object', {
#             'object': obj
#         })
