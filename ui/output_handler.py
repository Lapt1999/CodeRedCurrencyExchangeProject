
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