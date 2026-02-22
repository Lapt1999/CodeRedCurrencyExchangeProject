def display_transaction(action, source_currency, target_currency, amount, result):
    print(f'\n{action.capitalize()}: {amount:.2f} {source_currency} = {result:.2f} {target_currency}')

def display_rates(base, rates):
    print(f'\nBase currency: {base}')
    print('\nExchange rates\n')
    for currency, rate in rates.items():
        print(f'{currency}: {rate}')