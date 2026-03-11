from unittest.mock import patch

import pytest

from services.rate_service import get_rates, validate_target_currency, RateServiceError, UnsupportedCurrencyError

@patch('services.rate_service.get_latest_rate_by_api')
def test_get_rates_success(mock_api):
    mock_api.return_value = ('USD', {'EUR': 0.9, 'JPY': 140})

    base, rates = get_rates('USD')

    assert base == 'USD'
    assert rates == {'EUR': 0.9, 'JPY': 140}

@patch('services.rate_service.get_latest_rate_by_api')
def test_get_rates_failure(mock_api):
    mock_api.return_value = (None, None)

    with pytest.raises(RateServiceError):
        get_rates('USD')

def test_validate_target_currency_success():
    rates = {'EUR': 0.9, 'JPY': 140}
    validate_target_currency('EUR', rates, 'USD')

def test_validate_target_currency_failure():
    rates = {'EUR': 0.9, 'JPY': 140}

    with pytest.raises(UnsupportedCurrencyError):
        validate_target_currency('ABC', rates, 'USD')