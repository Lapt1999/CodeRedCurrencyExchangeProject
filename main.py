# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from services.rate_lolader import initialize_currencies_and_display
from ui.input_handler import get_main_action
from handlers import handle_conversion, handle_create_order, handle_check_order, handle_view_orders

def main():

    print('\nWelcome to Currency Exchange App')

    base, rates = initialize_currencies_and_display()

    if not base or not rates:
        return

    while True:

        main_action = get_main_action()

        # ------------------------------------- CONVERSION ------------------------------------------------------------

        if main_action == '1':

            handle_conversion(base, rates)

    # ---------------------------------------CREATE ORDER -------------------------------------------------------------

        elif main_action == '2':

            handle_create_order(base, rates)

    # ---------------------------------------CHECK ORDERS -------------------------------------------------------------

        elif main_action == '3':

            handle_check_order(base, rates)

    # --------------------------------------- VIEW ORDERS -------------------------------------------------------------

        elif main_action == '4':

            handle_view_orders()

    # ---------------------------------------------- EXIT -------------------------------------------------------------

        else:

            print('\nThank you for using Currency Exchange App')
            break


if __name__ == '__main__':
    main()