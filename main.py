# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from services.rate_lolader import initialize_currencies_and_display
from storage.data_storage import save_rates_to_csv
from services.converter import safe_process_transaction
from services.trend_service import analyze_and_suggest
from ui.input_handler import (get_action, get_amount, get_repeat, get_valid_target_currency,
                              get_valid_source_currency)
from ui.output_handler import display_transaction
from visualization.charts import all_charts

def main():

    print('\nWelcome to Currency Exchange App')

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

        # Saving data to csv
        save_rates_to_csv(base, rates)

        # Displaying a chart for target currency

        all_charts(base,source_currency, target_currency)

        # Analyzing a trend and displaying recommendation

        analyze_and_suggest(base, source_currency, target_currency)

    # --------------------------------- ASK TO CONTINUE -------------------------------------------------------------

        if get_repeat() == 'no':
            print('\nThank you for using Currency Exchange App')
            break


if __name__ == '__main__':
    main()