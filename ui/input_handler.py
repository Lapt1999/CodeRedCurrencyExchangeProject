from services.rate_service import validate_target_currency,  UnsupportedCurrencyError, get_rates, RateServiceError

def get_action():
    # Ask user for action: buy or sell
    while True:
        action = input('Do you want to buy or sell? (buy / sell): ').strip().lower()
        if action in ('buy', 'sell'):
            return action
        print('Please enter either "buy" or "sell".')

def get_currency(prompt):
    while True:
        currency = input(prompt).strip().upper()
        if currency.isalpha() and len(currency) == 3:
            return currency
        print('Invalid source currency format. Use 3-letter code.')

def get_valid_target_currency(rates, source_currency):
    while True:
        target_currency = get_currency('Enter the target currency (e.g., EUR): ')

        try:
            validate_target_currency(target_currency, rates, source_currency)
            return target_currency
        except UnsupportedCurrencyError as e2:
            print(e2)

def get_valid_source_currency(base, rates):
    while True:
        source_currency = get_currency('Enter the source currency (e.g., USD): ')
        if source_currency == base or source_currency in rates:
            return source_currency
        print(f'Currency "{source_currency}" is not available. please try again.')

def get_amount(currency):
    while True:
        try:
            amount = float(input(f'Enter the amount in {currency}: '))
            if amount <= 0:
                print('Please enter a positive number.')
                continue
            return amount
        except ValueError:
            print('Error: please enter a numeric value.')

def get_repeat():
    while True:
        repeat = input('Do you want to perform another conversion? (yes/no): ').strip().lower()
        if repeat in ('yes', 'no'):
            return repeat
        print('Please enter either "yes" or "no".')