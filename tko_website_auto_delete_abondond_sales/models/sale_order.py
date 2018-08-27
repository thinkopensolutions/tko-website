
from odoo import api, models, fields
from datetime import datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTF

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def auto_vaccume_abonded_sales(self):
        hours = self.env['ir.config_parameter'].get_param('website_sale_auto_vacuum')
        try:
            hours = int(hours)
        except:
            hours = 1
        expiry_date = fields.Datetime.to_string(datetime.today() - timedelta(hours=hours))
        orders = self.env['sale.order'].search([('state','in',['draft','cancel']),('partner_id.id', '=', self.env.ref('base.public_partner').id),('date_order','<',expiry_date)])
        orders.unlink()
        print ("total orders found............", len(orders))
        return True