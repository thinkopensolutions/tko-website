# -*- coding: utf-8 -*-
import odoo.addons.website_coupon.controllers.main as main
import odoo.addons.tko_br_website_sale.controllers.main as smain
from odoo import http, tools, _
from odoo.http import request


class BrWebsiteSaleCoupon(main.WebsiteCoupon):

    # Set Valid/invalid flag to show/hide warning
    # coupon_not_available

    @http.route(['/shop/cart'], type='http', auth="public", website=True)
    def cart(self, **post):
        order = request.website.sale_get_order()
        ICPSudo = request.env['ir.config_parameter'].sudo()
        if order:
            from_currency = order.company_id.currency_id
            to_currency = order.pricelist_id.currency_id
            compute_currency = lambda price: from_currency.compute(price, to_currency)
        else:
            compute_currency = lambda price: price
        valid = True
        coupon_product = request.env.ref("website_coupon.discount_product")
        if ICPSudo.get_param('tko_br_website_sale.sale_freight_warning') == 's' and len(
                set([line.product_id.has_frete for line in order.order_line if line.product_id and line.product_id != coupon_product])) > 1:
            valid = False

        values = {
            'website_sale_order': order,
            'compute_currency': compute_currency,
            'suggested_products': [],
            'valid': valid,
        }

        if order:
            _order = order
            if not request.env.context.get('pricelist'):
                _order = order.with_context(pricelist=order.pricelist_id.id)
            values['suggested_products'] = _order._cart_accessories()

        if post.get('type') == 'popover':
            return request.render("website_sale.cart_popover", values)

        if post.get('code_not_available'):
            values['code_not_available'] = post.get('code_not_available')
        elif post.get('coupon_not_available'):
            values['coupon_not_available'] = post.get('coupon_not_available')

        return request.render("website_sale.cart", values)


class BrWebsiteSaleCouponCheckout(smain.CorreiosL10nBrWebsiteSale):

    # fallback to "/shop/cart" if order not valid
    # Don't fallback just because website coupon, this is not to be considered
    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
        order = request.website.sale_get_order()
        ICPSudo = request.env['ir.config_parameter'].sudo()
        coupon_product = request.env.ref("website_coupon.discount_product")
        if ICPSudo.get_param('tko_br_website_sale.sale_freight_warning') == 's' and len(
                set([line.product_id.has_frete for line in order.order_line if line.product_id and line.product_id != coupon_product])) > 1:
            return request.redirect("/shop/cart")
        else:
            return super(smain.CorreiosL10nBrWebsiteSale, self).checkout(**post)


