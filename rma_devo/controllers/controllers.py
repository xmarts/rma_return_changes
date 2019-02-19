# -*- coding: utf-8 -*-
from odoo import http

# class RmaDevo(http.Controller):
#     @http.route('/rma_devo/rma_devo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rma_devo/rma_devo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rma_devo.listing', {
#             'root': '/rma_devo/rma_devo',
#             'objects': http.request.env['rma_devo.rma_devo'].search([]),
#         })

#     @http.route('/rma_devo/rma_devo/objects/<model("rma_devo.rma_devo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rma_devo.object', {
#             'object': obj
#         })