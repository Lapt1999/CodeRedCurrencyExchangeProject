
import csv
from datetime import datetime

from services.converter import calculate_cross_rate

class RateServiceError(Exception):
    pass

class UnsupportedCurrencyError(Exception):
    pass

def get_rates(base,rates):
    if base is None or rates is None:
        raise RateServiceError('Failed to get exchange rates. Please check the currency code and try again.')
    return base, rates

def validate_target_currency(target_currency, rates, source_currency):
    if target_currency not in rates:
        raise UnsupportedCurrencyError(f'{target_currency} is not supported for conversion from {source_currency}.')


def load_rates_from_scv(base, source, target, filename = 'data/exchange_rates.csv'):
    base, source, target = base.upper(), source.upper(), target.upper()

    all_rates = {}

    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
            currency = row['currency'].upper()
            rate = float(row['rate'])

            if date not in all_rates:
                all_rates[date] = {}
            all_rates[date][currency] = rate

    dates = sorted(all_rates.keys())
    cross_rates = []

    for date in  dates:
        rates_for_date = all_rates[date]
        if source not in rates_for_date or target not in rates_for_date:
            continue
        cross_rate = calculate_cross_rate(source, target, base, rates_for_date)
        cross_rates.append(cross_rate)

    return dates, cross_rates