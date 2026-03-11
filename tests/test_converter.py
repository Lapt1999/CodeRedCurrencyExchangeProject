import pytest
from services.converter import buy, sell

def test_buy():
    assert buy(20, 3) == 60

def test_sell():
    assert sell(80, 4) == 20
