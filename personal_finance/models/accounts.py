# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceAccounts(models.Model):
    _name = 'finance.accounts'
    _description = 'Finance Accounts'

    name = fields.Char()
