
def displaying_current_rate(source, target, calculated_rate):
    print(f'\nCurrent rate: {source}/{target} = {calculated_rate:.4f}')

def display_transaction(action, source_currency, target_currency, amount, result):
    print(f'\n{action.capitalize()}: {amount:.2f} {source_currency} = {result:.2f} {target_currency}')

def display_rates(base, rates):
    print(f'\nBase currency: {base}')
    print('\nExchange rates\n')
    for currency, rate in rates.items():
        print(f'{currency}: {rate}')

def display_currencies_only(base, rates):
    print(f'\nSupported currencies for conversion:\n')

    currencies = list(rates.keys())
    per_row = 48

    for i in range (0, len(currencies), per_row):
        row = currencies[i:i+per_row]
        print(' '.join(row))

    print('')

def display_executed_orders(executed):
    if executed:
        print('\nExecuted orders:\n')
        for e in executed:
            print(e)
    else:
        print('\nNo orders executed\n')

def display_orders(orders):
    if not orders:
        print('\nNo active orders')
        return

    for i, order in enumerate(orders, start = 1):
        print(
            f"\n{i}. {order['type'].upper()} | "
            f"{order['action'].upper()} | "
            f"{order['source_currency']} --> {order['target_currency']} | "
            f"Price: {order['price']} | "
            f"Amount: {order['amount']}"
        )
        print('')

def display_order_help():

    print("\nOrder types explanation:\n")

    print("STOP BUY  → Buy when price goes UP to your level (trend following)")
    print("STOP SELL → Sell when price goes DOWN to your level (stop loss)")

    print("LIMIT BUY  → Buy at your price or LOWER (buy cheaper)")
    print("LIMIT SELL → Sell at your price or HIGHER (sell for more)\n")


def suggest_order(trend):

    print("Order suggestion:")

    if trend == 'UP':
        print("Market is going UP")
        print("→ Consider STOP BUY (follow the trend)")
        print("→ Or LIMIT SELL (sell at higher price)\n")

    elif trend == 'DOWN':
        print("Market is going DOWN")
        print("→ Consider STOP SELL (protect from loss)")
        print("→ Or LIMIT BUY (buy cheaper)\n")

    else:
        print("Market is STABLE")
        print("→ Consider LIMIT orders (wait for better price)\n")