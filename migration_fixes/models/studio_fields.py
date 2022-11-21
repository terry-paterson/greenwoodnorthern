# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderInh(models.Model):
    _inherit = 'sale.order'

    @api.depends('company_id')
    def _compute_branch_ids(self):
        for rec in self:
            rec['x_branch_ids'] = rec.company_id.x_branch_1 + rec.company_id.x_branch_2 + rec.company_id.x_branch_3

    x_branch_id = fields.Many2one('res.partner', string='Branch', store=True)
    x_branch_ids = fields.Many2many('res.partner', compute="_compute_branch_ids", string='Branch', readonly=True)
    x_sale_order_line_ids_e9dcf = fields.One2many('x_sale_order_line_20330', 'x_sale_order_id', string='New Lines', store=True)
    x_studio_branch = fields.Char(related="x_branch_id.name", string='Channel', readonly=True, store=True)
    x_studio_brand = fields.Char(related="x_branch_id.name", string='Brand', readonly=True, store=True)
    x_studio_char_field_LUE79 = fields.Char(string='X Studio Char Field Lue79', store=True)
    x_studio_delivery_address = fields.Char(related="partner_id.contact_address", string='Delivery Address', readonly=True)
    x_studio_delivery_address_1 = fields.Char(related="partner_id.contact_address_complete", string='Delivery Address', readonly=True, store=True)
    x_studio_delivery_address_2 = fields.Selection(related='partner_id.type', string='Delivery Address', readonly=True, store=True)
    x_studio_expiration = fields.Char(string='Expiration', store=True)
    x_studio_many2many_field_PFJWE = fields.Many2many('crm.team', 'x_crm_team_sale_order_rel', 'sale_order_id', 'crm_team_id', string='Sales Team', store=True)
    x_studio_many2many_field_ZQSQ1 = fields.Many2many('crm.team.member', 'x_crm_team_member_sale_order_rel', 'sale_order_id', 'crm_team_member_id', string='Sales Team Member', store=True)
    x_studio_many2many_field_b6fTg = fields.Many2many('res.partner', 'x_res_partner_sale_order_rel', 'sale_order_id', 'res_partner_id', string='Contact', store=True)
    x_studio_payment_terms = fields.Selection(related='partner_id.x_studio_terms', string="Payment Terms", readonly=True, store=True)
    x_studio_po_reference = fields.Char(string='PO Reference', store=True)
    x_studio_related_field_TgW6e = fields.Selection(related='partner_shipping_id.type', string="New Related Field", readonly=True, store=True)
    x_studio_related_field_hP5kF = fields.Char(related="payment_term_id.name", string='New Related Field', readonly=True, store=True)
    x_studio_related_field_jYYTZ = fields.Many2one(related='user_id', string='Responsible', readonly=True, store=True)
    x_studio_related_field_y4LAm = fields.Char(related="partner_id.ref", string='New Related Field', readonly=True, store=True)


class SaleOrderInh(models.Model):
    _inherit = 'res.company'

    x_branch_1 = fields.Many2one('res.partner', string='Branch 1', store=True)
    x_branch_2 = fields.Many2one('res.partner', string='Branch 2', store=True)
    x_branch_3 = fields.Many2one('res.partner', string='Branch 3', store=True)



