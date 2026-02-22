from api.exchange_api import get_latest_rate_by_api

class RateServiceError(Exception):
    pass

class UnsupportedCurrencyError(Exception):
    pass

def get_rates(source_currency):
    base, rates = get_latest_rate_by_api(source_currency)
    if base is None or rates is None:
        raise RateServiceError('Failed to get exchange rates. Please check the currency code and try again.')
    return base, rates

def validate_target_currency(target_currency, rates, source_currency):
    if target_currency not in rates:
        raise UnsupportedCurrencyError(f'{target_currency} is not supported for conversion from {source_currency}.')
