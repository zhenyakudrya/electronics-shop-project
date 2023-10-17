import pytest
from src.phone import *
from tests.test_item import item


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test___repr__(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test___str__(phone):
    assert str(phone) == 'iPhone 14'


def test___add__(phone, item):
    assert item + phone == 25
    assert phone + phone == 10


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
        phone.number_of_sim = 1.5
