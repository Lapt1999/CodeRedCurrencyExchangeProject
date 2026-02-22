# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from storage.data_storage import save_rates_to_csv
from services.converter import calculate_cross_rate,process_transaction
from ui.input_handler import (get_action, get_amount, get_repeat, get_valid_target_currency,
                              get_valid_source_currency)
from ui.output_handler import display_transaction, display_rates

def main():

    print('Welcome to Currency Exchange App')

    while True:

        # Ask user for action: buy or sell
        action = get_action()

    # ---------------------------- SOURCE CURRENCY -----------------------------------------------------------------

        # Ask user for source currency, validating input
        base, rates, source_currency = get_valid_source_currency()

    # ---------------------------- TARGET CURRENCY -----------------------------------------------------------------

        # Ask user for target currency, validating input
        target_currency = get_valid_target_currency(rates, source_currency)

    # --------------------------------- AMOUNT -----------------------------------------------------------------

        # Ask user for the amount, validating user input
        amount = get_amount(source_currency)

    # --------------------------------- CALCULATION -----------------------------------------------------------------

        # Calculating an exchange rate
        rate = calculate_cross_rate(source_currency, target_currency, base, rates)

        # Performing calculation depending on the chosen action
        result = process_transaction(action, amount, rate)

        # Displaying the conversion result
        display_transaction(action, source_currency, target_currency, amount, result)

        # Displaying all rates
        display_rates(base, rates)

        # Saving data to csv
        save_rates_to_csv(base, rates)

    # --------------------------------- ASK TO CONTINUE -------------------------------------------------------------

        if get_repeat('Do you want to perform another conversion? (yes/no): ') == 'no':
            break


if __name__ == '__main__':
    main()