# -*- coding: utf-8 -*-
# from odoo import http


# class PersonalFinance(http.Controller):
#     @http.route('/personal_finance/personal_finance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/personal_finance/personal_finance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('personal_finance.listing', {
#             'root': '/personal_finance/personal_finance',
#             'objects': http.request.env['personal_finance.personal_finance'].search([]),
#         })

#     @http.route('/personal_finance/personal_finance/objects/<model("personal_finance.personal_finance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('personal_finance.object', {
#             'object': obj
#         })
