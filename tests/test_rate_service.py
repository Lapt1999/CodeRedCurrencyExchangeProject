from unittest.mock import patch

import pytest

from services.rate_service import get_rates, validate_target_currency, RateServiceError, UnsupportedCurrencyError


def test_get_rates_success():
    base = 'USD'
    rates = {'EUR': 0.9}

    result_base, result_rates = get_rates(base, rates)

    assert result_base == 'USD'
    assert result_rates == {'EUR': 0.9}


def test_get_rates_base_none():
    rates = {'EUR': 0.9}

    with pytest.raises(RateServiceError):
        get_rates(None, rates)


def test_get_rates_rates_empty():
    base = 'USD'

    with pytest.raises(RateServiceError):
        get_rates(base, None)


def test_validate_target_currency_success():
    rates = {'EUR': 0.9, 'JPY': 140}
    validate_target_currency('EUR', rates, 'USD')

def test_validate_target_currency_failure():
    rates = {'EUR': 0.9, 'JPY': 140}

    with pytest.raises(UnsupportedCurrencyError):
        validate_target_currency('ABC', rates, 'USD')


def test_validate_target_currency_error_message():
    rates = {'EUR': 0.9, 'JPY': 140}
    with pytest.raises(UnsupportedCurrencyError) as er:
        validate_target_currency('ABC', rates, 'USD')

    assert 'ABC is not supported' in str(er.value)