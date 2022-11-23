# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    purchase_price = fields.Float(
        string="Cost", compute="_compute_purchase_price",
        digits='Product Price', store=True, precompute=True,
        groups="base.group_user", readonly=False)

    @api.depends('product_id', 'company_id', 'currency_id', 'product_uom')
    def _compute_purchase_price(self):
        for line in self:
            if not line.product_id:
                line.purchase_price = 0.0
                continue
            line = line.with_company(line.company_id)
            product_cost = line.product_id.standard_price
            line.purchase_price = line._convert_price(product_cost, line.product_id.uom_id)
