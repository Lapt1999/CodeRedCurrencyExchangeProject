import csv
import os
from datetime import datetime

def save_rates_to_csv(data, filename='data/exchange_rates.csv'):

    # Checking if data was returned by API, if not - exit function

    if not data:
        print('No data to save.')
        return

    rates = data['rates']
    base = data['base_code']
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Checking if file already exists

    if_file_exists = os.path.isfile(filename)

    with open(filename, mode = 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Adding a header if creating file for the first time

        if not if_file_exists:
            header = [date, base] + list(rates.keys())
            writer.writerow(header)

        # Adding a row

        row = [date, base] + list(rates.values())
        writer.writerow(row)

    print('Data successfully saved to csv file.')