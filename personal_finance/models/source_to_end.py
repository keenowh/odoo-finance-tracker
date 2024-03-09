# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SourceToEnd(models.Model):
    _name = 'source.to.end'
    _description = 'Source to End'

    name = fields.Char()
    account_source = fields.Many2one('finance.accounts', 'Account Source')
    account_end = fields.Many2one('finance.accounts', 'Account End')
    finance_entry_ids = fields.One2many('finance.entries', 'source_to_end_id', 'Finance Entries')
