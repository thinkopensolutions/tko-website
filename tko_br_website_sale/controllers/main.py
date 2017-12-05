# -*- coding: utf-8 -*-
import odoo.addons.website_sale.controllers.main as main
from odoo import http, tools, _
from odoo.http import request


class CorreiosL10nBrWebsiteSale(main.WebsiteSale):
    def checkout_form_validate(self, mode, all_form_values, data):
        errors, error_msg = super(CorreiosL10nBrWebsiteSale, self). \
            checkout_form_validate(mode, all_form_values, data)
        # FUll name is not passed to cielo if name doesn't have space in it
        if 'name' in data and data['name']:
            data['name'] = data['name'].strip()
            if len(data['name'].split(" ")) < 2:
                errors["name"] = u"invalid"
                error_msg.append(u'Nome deve conter o Primeiro e Último nome')

        # bug on correios if phone length is not valid
        if 'phone' in data and data['phone']:
            phone_length = len([digit for digit in data['phone'] if digit.isdigit()])
            if phone_length < 10 or phone_length > 11:
                errors["phone"] = u"invalid"
                error_msg.append(u'Telefone deve conter no mínimo 10 e no máximo 11 caracteres')
        return errors, error_msg

    # Set Valid/invalid flag to show/hide warning

    @http.route(['/shop/cart'], type='http', auth="public", website=True)
    def cart(self, **post):
        order = request.website.sale_get_order()
        if order:
            from_currency = order.company_id.currency_id
            to_currency = order.pricelist_id.currency_id
            compute_currency = lambda price: from_currency.compute(price, to_currency)
        else:
            compute_currency = lambda price: price
        valid = True
        if order.company_id.sale_freight_warning == 's' and len(set([line.product_id.has_frete for line in order.order_line if line.product_id])) > 1:
            valid = False

        values = {
            'website_sale_order': order,
            'compute_currency': compute_currency,
            'suggested_products': [],
            'valid':valid,
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

        return request.render("website_sale.cart", values)

    # fallback to "/shop/cart" if order not valid
    @http.route(['/shop/checkout'], type='http', auth="public", website=True)
    def checkout(self, **post):
        order = request.website.sale_get_order()
        if order.company_id.sale_freight_warning == 's' and len(set([line.product_id.has_frete for line in order.order_line if line.product_id])) > 1:
            return request.redirect("/shop/cart")
        else:
            return super(CorreiosL10nBrWebsiteSale, self).checkout(**post)
