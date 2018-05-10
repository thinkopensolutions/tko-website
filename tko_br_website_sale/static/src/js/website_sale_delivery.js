'use strict';
odoo.define('tko_br_website_sale.checkout', function (require) {

    require('web.dom_ready');
    var ajax = require('web.ajax');

    /* Handle interactive carrier choice + cart update */
    var $pay_button = $('#o_payment_form_pay');

    var _onCarrierUpdateAnswer = function(result) {
        var $amount_delivery = $('#order_delivery span.oe_currency_value');
        var $amount_untaxed = $('#order_total_untaxed span.oe_currency_value');
        var $amount_tax = $('#order_total_taxes span.oe_currency_value');

        $('#order_total_frete span.oe_currency_value');
        var $amount_total = $('#order_total span.oe_currency_value');
        var $carrier_badge = $('#delivery_carrier input[name="delivery_type"][value=' + result.carrier_id + '] ~ .badge.hidden');
        var $compute_badge = $('#delivery_carrier input[name="delivery_type"][value=' + result.carrier_id + '] ~ .o_delivery_compute');
        var $amount_frete = $('#order_total_frete span.oe_currency_value');
        if (result.status === true) {
            $amount_delivery.text(result.new_amount_delivery);
            console.log("deliverystandard local...........",$amount_delivery);
            $amount_untaxed.text(result.new_amount_untaxed);
            $amount_frete.text(result.new_amount_delivery);
            $amount_tax.text(result.new_amount_tax);
            $amount_total.text(result.new_amount_total);
            $carrier_badge.children('span').text(result.new_amount_delivery);
            $carrier_badge.removeClass('hidden');
            $compute_badge.addClass('hidden');
            $pay_button.prop('disabled', false);
        }
        else {
            console.error(result.error_message);
            $compute_badge.text(result.error_message);
        }
    };

    var _onCarrierClick = function(ev) {
        $pay_button.prop('disabled', true);
        var carrier_id = $(ev.currentTarget).val();
        var values = {'carrier_id': carrier_id};
        ajax.jsonRpc('/shop/update_carrier', 'call', values)
          .then(_onCarrierUpdateAnswer);
    };

    var $carriers = $("#delivery_carrier input[name='delivery_type']");
    $carriers.click(_onCarrierClick);

    /* Handle stuff */

});
