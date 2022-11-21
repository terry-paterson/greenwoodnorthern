# -*- coding: utf-8 -*-

from odoo import models, fields, api

class x_suppliers(models.Model):
    _name = 'x_suppliers'
    _description = "Suppliers"

    x_active = fields.Boolean('Active', store=True)
    x_name = fields.Char(string='Name', required=True, store=True)
    x_studio_char_field_X3rpc = fields.Char(string='New Text', store=True)
    x_studio_partner_email = fields.Char(related="x_studio_partner_id.email", string='Email', store=True)
    x_studio_partner_id = fields.Many2one('res.partner', string='Contact', store=True)
    x_studio_partner_phone = fields.Char(related="x_studio_partner_id.phone", string='Phone', store=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)
    x_suppliers_line_ids_86ceb = fields.One2many('x_suppliers_line_9892a', 'x_suppliers_id', string='X Suppliers Line Ids 86Ceb', store=True)
    x_suppliers_line_ids_8b03e = fields.One2many('x_suppliers_line_abd43', 'x_suppliers_id', string='New Lines', store=True)
    x_suppliers_line_ids_f94cc = fields.One2many('x_suppliers_line_0a4e2', 'x_suppliers_id', string='New Lines', store=True)


class x_sale_order_line_20330(models.Model):
    _name = 'x_sale_order_line_20330'
    _description = "sale_order_line"

    display_name = fields.Char(string='Display Name', readonly=True)
    x_name = fields.Char(string='Description', required=True, store=True)
    x_sale_order_id = fields.Many2one('sale.order', string='X Sale Order', store=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)


class x_suppliers_line_9892a(models.Model):
    _name = 'x_suppliers_line_9892a'
    _description = "suppliers_line"

    display_name = fields.Char(string='Display Name', readonly=True)
    x_name = fields.Char(string='Description', required=True, store=True)
    x_suppliers_id = fields.Many2one('x_suppliers', string='X Suppliers', store=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)


class x_suppliers_line_abd43(models.Model):
    _name = 'x_suppliers_line_abd43'
    _description = "suppliers_line"

    display_name = fields.Char(string='Display Name', readonly=True)
    x_name = fields.Char(string='Description', required=True, store=True)
    x_suppliers_id = fields.Many2one('x_suppliers', string='X Suppliers', store=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)


class x_suppliers_line_0a4e2(models.Model):
    _name = 'x_suppliers_line_0a4e2'
    _description = "suppliers_line"

    display_name = fields.Char(string='Display Name', readonly=True)
    x_name = fields.Char(string='Description', required=True, store=True)
    x_suppliers_id = fields.Many2one('x_suppliers', string='X Suppliers', store=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)
