# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_freight_warning = fields.Selection([
        ('s', 'Sale with and without freight separately'),
        ('t', 'Sale all type of products'),
    ], string='Freight Warning',
        required=True,
        default='together',
        help='Sale with and without freight separately: You can either buy with or without delivery charges products in one time.\n'
             'Sale all type of products together: you can buy with and without delivery charges products together\n'
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update({'sale_freight_warning' : ICPSudo.get_param('tko_br_website_sale.sale_freight_warning')})
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param("tko_br_website_sale.sale_freight_warning", self.sale_freight_warning)
