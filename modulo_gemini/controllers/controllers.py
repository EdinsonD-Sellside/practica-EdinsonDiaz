# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloGemini(http.Controller):
#     @http.route('/modulo_gemini/modulo_gemini', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_gemini/modulo_gemini/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_gemini.listing', {
#             'root': '/modulo_gemini/modulo_gemini',
#             'objects': http.request.env['modulo_gemini.modulo_gemini'].search([]),
#         })

#     @http.route('/modulo_gemini/modulo_gemini/objects/<model("modulo_gemini.modulo_gemini"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_gemini.object', {
#             'object': obj
#         })

