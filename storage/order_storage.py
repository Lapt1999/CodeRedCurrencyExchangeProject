
import csv

def save_orders_to_scv(orders, filename='data/orders.csv'):

    with open(filename, mode = 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['type', 'action', 'source_currency', 'target_currency', 'price', 'amount'])

        for order in orders:
            writer.writerow([order['type'], order['action'], order['source_currency'], order['target_currency'],
                             order['price'], order['amount']])


def load_orders_from_scv(filename='data/orders.csv'):

    orders = []

    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                orders.append({
                    'type': row['type'],
                    'action': row['action'],
                    'source_currency': row['source_currency'],
                    'target_currency': row['target_currency'],
                    'price': float(row['price']),
                    'amount': float(row['amount'])
                })

    except FileNotFoundError:
        return []

    return orders