import pytest
from unittest.mock import patch
from services.converter import buy, sell, calculate_cross_rate, process_transaction, safe_process_transaction

rates = {
    'USD': 1.0,
    'EUR': 0.9,
    'JPY': 110.0
}

def test_same_currency_return_1():
    assert calculate_cross_rate('USD', 'USD', 'USD', rates) == 1

def test_base_to_other_currency():
    assert calculate_cross_rate('USD', 'EUR', 'USD', rates) == 0.9

def test_other_currency_to_base():
    assert calculate_cross_rate('EUR', 'USD', 'USD', rates) == 1/0.9

def test_cross_currency_conversion():
    assert calculate_cross_rate('EUR', 'JPY', 'USD', rates) == 110.0/0.9

def test_source_not_in_rates_raises():
    with pytest.raises(ValueError):
        calculate_cross_rate('ABS', 'USD', 'USD', rates)

def test_target_not_in_rates_raises():
    with pytest.raises(ValueError):
        calculate_cross_rate('USD', 'ABS', 'USD', rates)

def test_buy_calculation():
    assert buy(100, 1.5) == 150

def test_sell_calculation():
    assert sell(150, 1.5) == 100

def test_process_transaction_buy():
    assert process_transaction('buy', 100, 1.5) == 150

def test_process_transaction_sell():
    assert process_transaction('sell', 150, 1.5) == 100

@patch('services.converter.process_transaction')
@patch('services.converter.calculate_cross_rate')
def test_safe_process_transaction_success(mock_rate, mock_process):
    mock_rate.return_value = 1.5
    mock_process.return_value = 150

    success, result = safe_process_transaction('USD', 'EUR', 'USD', {}, 100, 'buy')

    assert success == True
    assert result == 150
    mock_rate.assert_called_once_with('USD', 'EUR', 'USD', {})
    mock_process.assert_called_once_with('buy', 100, 1.5)

@patch('services.converter.calculate_cross_rate', side_effect = ValueError('Value error!'))
def test_safe_process_transaction_success_value_error(mock_rate):
    success, result = safe_process_transaction('USD', 'EUR', 'USD', {}, 100, 'buy')

    assert success == False
    assert 'Value error!' in result

@patch('services.converter.calculate_cross_rate', side_effect = Exception('Unexpected error!'))
def test_safe_process_transaction_success_unexpected_error(mock_rate):
    success, result = safe_process_transaction('USD', 'EUR', 'USD', {}, 100, 'buy')

    assert success == False
    assert 'Unexpected error!' in result