import csv

from storage.data_storage import save_rates_to_csv

def test_save_rates_to_csv_no_data(tmp_path, capsys):
    filename = tmp_path / 'rates.scv'

    save_rates_to_csv(None, None, filename)

    captured = capsys.readouterr()

    assert captured.out == 'No data to save.\n'
    assert not filename.exists()

def test_save_rates_to_scv_create_file(tmp_path):
    filename = tmp_path / 'rates.scv'
    base = 'USD'
    rates = {'EUR': 0.9, 'GBP': 0.8}

    save_rates_to_csv(base, rates, filename)

    assert filename.exists()

    with open(filename, newline= '') as f:
        reader = list(csv.reader(f))

    assert reader[0] == ['date', 'base', 'currency', 'rate']
    assert reader[1][1:] == ['USD', 'EUR', '0.9']
    assert reader[2][1:] == ['USD', 'GBP', '0.8']

def test_save_rates_to_csv_append_file(tmp_path):
    filename = tmp_path / 'rates.scv'
    base = 'USD'
    rates = {'EUR': 0.9}
    save_rates_to_csv(base, rates, filename)
    save_rates_to_csv(base, rates, filename)

    with open(filename, newline= '') as f:
        reader = list(csv.reader(f))

    assert reader[0] == ['date', 'base', 'currency', 'rate']
    assert len(reader) == 3



