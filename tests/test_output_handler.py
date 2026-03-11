from ui.output_handler import display_transaction, display_rates

def test_display_transaction(capsys):
    display_transaction('buy', 'USD', 'EUR', 100, 90)
    captured = capsys.readouterr()

    assert captured.out == '\nBuy: 100.00 USD = 90.00 EUR\n'

def test_display_rates(capsys):
    rates = {
        'EUR': 0.9,
        'GBP': 0.8
    }
    display_rates('USD', rates)

    captured = capsys.readouterr()

    expected_output = (
        '\nBase currency: USD\n'
        '\nExchange rates\n\n'
        'EUR: 0.9\n'
        'GBP: 0.8\n'
    )

    assert captured.out == expected_output