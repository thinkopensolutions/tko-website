# -*- encoding: utf-8 -*-

from odoo import models, api, fields, _


class res_company(models.Model):
    _inherit = 'res.company'

    sale_freight_warning = fields.Selection([
        ('s', 'Sale with and without freight separately'),
        ('t', 'Sale all type of products together'),
    ], string='Freight Warning',
        required=True,
        default='t',
        help='Sale with and without freight separately: You can either buy with or without delivery charges products in one time.\n'
             'Sale all type of products: you can buy with and without delivery charges products together\n'
    )
