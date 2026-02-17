# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from api.exchange_api import get_latest_rate
from storage.data_storage import save_rates_to_csv
from services.converter import calculate_cross_rate, buy, sell

def main():

    print('Welcome to Currency Exchange App')

    program_running = True

    while program_running:

        # Ask user for action: buy or sell
        while True:
            action = input('Do you want to buy or sell? (buy / sell): ').strip().lower()
            if action not in ('buy', 'sell'):
                print('Please enter either "buy" or "sell".')
            else:
                break

    # ---------------------------- SOURCE CURRENCY -----------------------------------------------------------------

        while True:
            # Ask user for source currency, validating input
            source_currency = input('Enter the source currency (e.g., USD): ').strip().upper()
            if not source_currency.isalpha() or len(source_currency) != 3:
                print('Invalid source currency format. Use 3-letter code.')
                continue

            # Getting rates from API
            base, rates = get_latest_rate(source_currency)

            # Checking if the currency entered by user exists
            if base is None or rates is None:
                print('Failed to get exchange rates. Please check the currency code and try again.')
                continue
            else:
                break

    # ---------------------------- TARGET CURRENCY -----------------------------------------------------------------

        while True:
            # Ask user for target currency, validating input
            target_currency = input('Enter the target currency (e.g., EUR): ').strip().upper()
            if not target_currency.isalpha() or len(target_currency) != 3:
                    print('Invalid target currency format. Use 3-letter code.')
                    continue

            if target_currency not in rates.keys():
                print(f'{target_currency} is not supported for conversion from {source_currency}.')
                continue
            else:
                break

    # --------------------------------- AMOUNT -----------------------------------------------------------------

        # Ask user for the amount, validating user input
        while True:
            try:
                amount = float(input(f'Enter the amount in {source_currency}: '))
                break
            except ValueError:
                print('Error: please enter a numeric value.')

    # --------------------------------- CALCULATION -----------------------------------------------------------------

        # Calculating an exchange rate
        rate = calculate_cross_rate(source_currency, target_currency, base, rates)

        # Performing calculation depending on the chosen action
        if action == 'buy':
            result = buy(amount, rate)
            print(f'\nBuying: {amount:.2f} {source_currency} = {result:.2f} {target_currency}')
        else:
            result = sell(amount, rate)
            print(f'\nSelling: {amount:.2f} {source_currency} = {result:.2f} {target_currency}')

        if base or rates:
            print(f'\nBase currency: {base}')
            print('\nExchange rates\n')
            for currency, rate in rates.items():
                print(f'{currency}: {rate}')

            # Saving data to csv

            save_rates_to_csv(base, rates)

        else:
            print('Failed to fetch data.')

    # --------------------------------- ASK TO CONTINUE -------------------------------------------------------------

        while True:
            repeat = input('Do you want to perform another conversion? (yes/no): ').strip().lower()
            if repeat not in ('yes', 'no'):
                print('Please enter either "yes" or "no".')
            else:
                if repeat == 'no':
                    program_running = False
                break


if __name__ == '__main__':
    main()