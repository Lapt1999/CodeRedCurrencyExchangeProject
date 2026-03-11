from unittest.mock import patch, Mock

import requests

from api.exchange_api import get_latest_rate_by_api


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_success(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        'result': 'success',
        'base_code': 'USD',
        'rates': {'EUR': 0.9}
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    base, rates = get_latest_rate_by_api('usd')

    assert base == 'USD'
    assert rates == {'EUR': 0.9}


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_error(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        'result': 'error'
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    base, rates = get_latest_rate_by_api('usd')

    assert base is None
    assert rates is None


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    base, rates = get_latest_rate_by_api('usd')

    assert base is None
    assert rates is None


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError

    base, rates = get_latest_rate_by_api('usd')

    assert base is None
    assert rates is None


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError

    base, rates = get_latest_rate_by_api('usd')

    assert base is None
    assert rates is None


@patch('api.exchange_api.requests.get')
def test_get_latest_rate_by_api_unexpected_error(mock_get):
    mock_get.side_effect = Exception

    base, rates = get_latest_rate_by_api('usd')

    assert base is None
    assert rates is None