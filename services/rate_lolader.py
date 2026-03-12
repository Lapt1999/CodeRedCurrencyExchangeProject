
from api.exchange_api import get_latest_rate_by_api
from ui.output_handler import display_currencies_only
from services.rate_service import get_rates, RateServiceError


def initialize_currencies_and_display(base='EUR'):
    try:
        base, rates = get_latest_rate_by_api(base)
        base, rates = get_rates(base, rates)
    except RateServiceError as e:
        print(e)
        return None, None
    display_currencies_only(base, rates)
    return base, rates