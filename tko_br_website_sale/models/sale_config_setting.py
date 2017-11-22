# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    sale_freight_warning = fields.Selection([
        ('s', 'Sale with and without freight separately'),
        ('t', 'Sale all type of products'),
    ], string='Freight Warning',
        required=True,
        default='together',
        help='Sale with and without freight separately: You can either buy with or without delivery charges products in one time.\n'
             'Sale all type of products together: you can buy with and without delivery charges products together\n'
    )

    def get_default_sale_freight_warning(self, fields):
        return {'sale_freight_warning':
                    self.env.user.company_id.sale_freight_warning}

    @api.multi
    def set_default_sale_freight_warning(self):
        self.env.user.company_id.issue_eletronic_doc = self.sale_freight_warning
