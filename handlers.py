from ui.output_handler import display_order_help


def handle_conversion(base, rates):

    from ui.input_handler import (get_action, get_amount, get_valid_target_currency,
                              get_valid_source_currency)
    from services.converter import safe_process_transaction, calculate_cross_rate
    from ui.output_handler import display_transaction, displaying_current_rate
    from storage.data_storage import save_rates_to_csv
    from visualization.charts import all_charts
    from services.trend_service import analyze_and_suggest

    # Ask user for action: buy or sell
    action = get_action()

    # ---------------------------- SOURCE CURRENCY ------------------------------------------------------------

    # Ask user for source currency, validating input
    source_currency = get_valid_source_currency(base, rates)

    # ---------------------------- TARGET CURRENCY ------------------------------------------------------------

    # Ask user for target currency, validating input
    target_currency = get_valid_target_currency(rates, source_currency)

    current_rate = calculate_cross_rate(source_currency, target_currency, base, rates)

    displaying_current_rate(source_currency, target_currency, current_rate)

    # --------------------------------- AMOUNT ----------------------------------------------------------------

    # Ask user for the amount, validating user input
    amount = get_amount(source_currency)

    # --------------------------------- CALCULATION -----------------------------------------------------------

    # Calculating an exchange rate depending on the chosen action
    status, result = safe_process_transaction(source_currency, target_currency, base, rates, amount, action)

    # Displaying the conversion result
    display_transaction(action, source_currency, target_currency, amount, result)

    # Saving data to csv
    save_rates_to_csv(base, rates)

    # Displaying a chart for target currency
    all_charts(base, source_currency, target_currency)

    # Analyzing a trend and displaying recommendation
    analyze_and_suggest(base, source_currency, target_currency)


def handle_create_order(base, rates):

    from ui.output_handler import display_order_help
    from services.order_service import create_order
    from storage.order_storage import load_orders_from_scv, save_orders_to_scv

    # Displaying information about order types
    display_order_help()

    # Creating order
    order = create_order(base, rates)

    # Saving order to scv file
    orders = load_orders_from_scv()
    orders.append(order)
    save_orders_to_scv(orders)


def handle_check_order(base, rates):

    from storage.order_storage import load_orders_from_scv, save_orders_to_scv
    from services.order_service import check_orders
    from ui.output_handler import display_executed_orders


    orders = load_orders_from_scv()

    if not orders:
        print('\nNo active orders\n')
        return

    executed, updated_orders = check_orders(orders, base, rates)

    display_executed_orders(executed)

    save_orders_to_scv(updated_orders)


def handle_view_orders():

    from storage.order_storage import load_orders_from_scv
    from ui.output_handler import display_orders

    orders = load_orders_from_scv()

    display_orders(orders)