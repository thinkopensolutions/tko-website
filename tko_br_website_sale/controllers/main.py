# -*- coding: utf-8 -*-
import odoo.addons.website_sale.controllers.main as main


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
