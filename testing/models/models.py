# -*- coding: utf-8 -*-

from odoo import models, fields, api


class testing(models.Model):
    _inherit = 'res.partner'

    x_studio_category = fields.Selection([('Weekly', 'Weely'), ('Monthly', 'Monthly'), (
        'Yearly', 'Yearly')], string='Purchase Frequency')

    x_studio_company_type = fields.Selection(
        [('End User', 'End User'), ('Estate', 'Estate'), ('Hotel / Golf Course', 'Hotel / Golf Course'), ('Landscaper', 'Landscaper'),
         ('Shopify', 'Shopify'), ('DIY Livery', 'DIY Livery')], string='Company Type')

    x_studio_competitor = fields.Selection(
        [('Best 4 Hedging', 'Best 4 Hedging'), ('Growforth', 'Growforth'), ('Scot Plants', 'Scot Plants')],
        string='Competitor 1')

    x_studio_competitor_2 = fields.Selection(
        [('Best 4 Hedging', 'Best 4 Hedging'), ('Growforth', 'Growforth'), ('Scot Plants', 'Scot Plants')],
        string='Competitor 2')

    x_studio_email_invoice = fields.Boolean(string="Email Invoice")
    x_studio_est_annual_spend = fields.Char(string="Est Annual Spend")

    x_studio_invoice_email_address = fields.Char(string="Invoice Email Address")

    x_studio_supplier = fields.Boolean(string="Supplier")
    x_studio_terms = fields.Selection(
        [('Payment Due on Order', 'Payment Due on Order'), ('30 Days', '30 Days'), ('60 Days', '60 Days'), ('90 Days', '90 Days')],
        string='Terms')

    x_studio_visit = fields.Boolean(string="Visit")
