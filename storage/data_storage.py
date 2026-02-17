import csv
import os
from datetime import datetime

def save_rates_to_csv(base, rates, filename='data/exchange_rates.csv'):

    # Checking if data was returned by API, if not - exit function

    if not base or not rates:
        print('No data to save.')
        return

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Checking if file already exists

    if_file_exists = os.path.isfile(filename)

    with open(filename, mode = 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Adding a header if creating file for the first time

        if not if_file_exists:
            writer.writerow( ['date', 'base', 'currency', 'rate'])

        # Adding a row

        for currency, rate in rates.items():
            writer.writerow([date, base, currency, rate])


    print(f'Data successfully saved to csv file {filename}.')