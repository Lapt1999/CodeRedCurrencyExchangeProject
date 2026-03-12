def display_transaction(action, source_currency, target_currency, amount, result):
    print(f'\n{action.capitalize()}: {amount:.2f} {source_currency} = {result:.2f} {target_currency}')

def display_rates(base, rates):
    print(f'\nBase currency: {base}')
    print('\nExchange rates\n')
    for currency, rate in rates.items():
        print(f'{currency}: {rate}')

def display_currencies_only(base, rates):
    print(f'\nSupported currencies for conversion:')
    print(base)
    for currency in rates.keys():
        print(currency)