# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from api.exchange_api import get_latest_rate
from storage.data_storage import save_rates_to_csv

def main():

    print("Welcome to Currency Exchange App")

    # Getting data from API

    base_currency = input("Enter currency to convert from: ")

    data = get_latest_rate(base_currency)

    if data:
        print(f'\nBase currency: {data['base_code']}')
        print('\nExchange rates\n')
        rates = data['rates']
        for currency, rate in rates.items():
            print(f'{currency}: {rate}')

        # Saving data to csv

        save_rates_to_csv(data)

    else:
        print('Failed to fetch data.')


if __name__ == '__main__':
    main()