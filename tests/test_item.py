from src.item import *
import pytest


@pytest.fixture
def item():
    item = Item("Смартфон", 10000, 20)
    return item


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    assert item.price == 10000

