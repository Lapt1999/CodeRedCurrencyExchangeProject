from services.converter import calculate_cross_rate
from ui.input_handler import (get_order_type, get_action_for_order, get_valid_source_currency,
                              get_valid_target_currency,get_price_for_order, get_amount)

def create_order(base, rates):
    order_type_ = get_order_type()
    action = get_action_for_order()
    source_currency = get_valid_source_currency(base, rates)
    target_currency = get_valid_target_currency(rates, source_currency)
    price = get_price_for_order()
    amount = get_amount(source_currency)

    print('\nOrder successfully created\n')

    return {
        'type': order_type_,
        'action': action,
        'source_currency': source_currency,
        'target_currency': target_currency,
        'price': price,
        'amount': amount
    }


def check_orders(orders, base, rates):

    executed = []

    for order in orders:
        rate = calculate_cross_rate(order['source_currency'], order['target_currency'], base,rates)

        if order['type'] == 'stop':
            if order['action'] == 'buy' and rate >= order['price']:
                executed.append(order)
            elif order['action'] == 'sell' and rate <= order['price']:
                executed.append(order)

        elif order['type'] == 'limit':
            if order['action'] == 'buy' and rate <= order['price']:
                executed.append(order)
            elif order['action'] == 'sell' and rate >= order['price']:
                executed.append(order)

    for e in executed:
        orders.remove(e)

    return executed, orders