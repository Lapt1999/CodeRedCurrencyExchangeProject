from services.rate_service import validate_target_currency,  UnsupportedCurrencyError, get_rates, RateServiceError

def get_main_action():
    print('Choose action:')
    print('1 - Convert currency')
    print('2 - Create order')
    print('3 - Check orders')
    print('4 - View orders')
    print('5 - Exit\n')

    while True:
        choice = input('Your choice: ').strip()
        if choice in ('1', '2', '3', '4', '5'):
            return choice
        print('Please enter either "1" or "2" or "3" or "4" or "5"')

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
        if target_currency == source_currency:
            print('Target currency is equal to source currency.')
            continue
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

def get_order_type():
    while True:
        order_type = input('Please enter an order type (stop/limit): ').strip().lower()
        if order_type in ('stop', 'limit'):
            return order_type
        print('Please enter either "stop" or "limit".')

def get_action_for_order():
    while True:
        action = input('Please enter an action (buy/sell): ').strip().lower()
        if action in ('buy', 'sell'):
            return action
        print('Please enter either "buy" or "sell".')

def get_price_for_order():
    while True:
        try:
            price = float(input(f'Enter a target price: '))
            if price <= 0:
                print('Price must be greater than 0')
                continue
            return price
        except ValueError:
            print('Error: please enter a numeric value.')