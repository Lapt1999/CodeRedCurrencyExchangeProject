# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from services.rate_lolader import initialize_currencies_and_display
from storage.data_storage import save_rates_to_csv
from services.converter import safe_process_transaction
from ui.input_handler import (get_action, get_amount, get_repeat, get_valid_target_currency,
                              get_valid_source_currency)
from ui.output_handler import display_transaction, display_rates

def main():

    print('Welcome to Currency Exchange App')

    base, rates = initialize_currencies_and_display()

    if not base or not rates:
        return


    while True:

        # Ask user for action: buy or sell
        action = get_action()

    # ---------------------------- SOURCE CURRENCY -----------------------------------------------------------------

        # Ask user for source currency, validating input
        source_currency = get_valid_source_currency(base, rates)

    # ---------------------------- TARGET CURRENCY -----------------------------------------------------------------

        # Ask user for target currency, validating input
        target_currency = get_valid_target_currency(rates, source_currency)

    # --------------------------------- AMOUNT -----------------------------------------------------------------

        # Ask user for the amount, validating user input
        amount = get_amount(source_currency)

    # --------------------------------- CALCULATION -----------------------------------------------------------------

        # Calculating an exchange rate depending on the chosen action
        status, result = safe_process_transaction(source_currency, target_currency, base, rates, amount, action)

        # Displaying the conversion result
        display_transaction(action, source_currency, target_currency, amount, result)

        # Displaying all rates
        display_rates(base, rates)

        # Saving data to csv
        save_rates_to_csv(base, rates)

    # --------------------------------- ASK TO CONTINUE -------------------------------------------------------------

        if get_repeat() == 'no':
            print('Thank you for using Currency Exchange App')
            break


if __name__ == '__main__':
    main()