from unittest.mock import patch

from ui.input_handler import get_action, get_currency, get_amount, get_repeat, get_valid_target_currency, get_valid_source_currency

from services.rate_service import UnsupportedCurrencyError



@patch('builtins.input', side_effect=['test', 'buy'])
def test_get_action_buy(mock_input):
    result = get_action()
    assert result == 'buy'


@patch('builtins.input', side_effect=['test', 'sell'])
def test_get_action_sell(mock_input):
    result = get_action()
    assert result == 'sell'

@patch('builtins.input', side_effect=['sell'])
def test_get_action_direct(mock_input):
    result = get_action()
    assert result == 'sell'


@patch('builtins.input', side_effect=['84', 'usd'])
def test_get_currency(mock_input):
    result = get_currency('Enter currency: ')
    assert result == 'USD'


@patch('builtins.input', side_effect=['usd', '-5', '84'])
def test_get_amount(mock_input):
    result = get_amount('USD')
    assert result == 84


@patch('builtins.input', side_effect=['84'])
def test_get_amount_valid(mock_input):
    result = get_amount('Enter amount: ')
    assert result == 84


@patch('builtins.input', side_effect=['maybe', 'Yes'])
def test_get_repeat_yes(mock_input):
    result = get_repeat()
    assert result == 'yes'


@patch('builtins.input', side_effect=['maybe', 'No'])
def test_get_repeat_no(mock_input):
    result = get_repeat()
    assert result == 'no'


@patch('builtins.input', side_effect=['eur'])
@patch('ui.input_handler.validate_target_currency')
def test_get_valid_target_currency(mock_validate_target_currency, mock_input):
    rates = {'EUR': 0.9}
    result = get_valid_target_currency(rates, 'USD')
    assert result == 'EUR'


@patch('builtins.input', side_effect=['abc', 'eur'])
@patch('ui.input_handler.validate_target_currency', side_effect = [UnsupportedCurrencyError, None])
def test_get_valid_target_currency_retry(mock_validate_target_currency, mock_input):
    rates = {'EUR': 0.9}
    result = get_valid_target_currency(rates, 'USD')
    assert result == 'EUR'


@patch('builtins.input', return_value='usd')
def test_get_valid_source_currency_base(mock_input):
    result = get_valid_source_currency('USD', {'EUR': 0.9})
    assert result == 'USD'


@patch('builtins.input', return_value='eur')
def test_get_valid_source_currency_from_rates(mock_input):
    result = get_valid_source_currency('USD', {'EUR': 0.9})
    assert result == 'EUR'


@patch('builtins.input', side_effect=['aaa', 'usd'])
def test_get_valid_source_currency_retry(mock_input):
    result = get_valid_source_currency('USD', {'EUR': 0.9})
    assert result == 'USD'





