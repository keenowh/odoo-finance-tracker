# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FinanceEntries(models.Model):
    _name = 'finance.entries'
    _description = 'Finance Entries'

    name = fields.Char()
    account_source = fields.Many2one('finance.accounts', 'Account Source')
    account_end = fields.Many2one('finance.accounts', 'Account End')
    amount = fields.Float('Amount',2)
    description = fields.Char()
    remarks = fields.Char()
    transaction_date = fields.Date()
    target_date_of_payment = fields.Date()
    source_to_end_id = fields.Many2one('source.to.end', "Source to End")
    # credit_card_statement_id = field


