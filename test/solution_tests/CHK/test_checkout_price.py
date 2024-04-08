import pytest

from lib.solutions.CHK.checkout_solution import checkout, count_skus, calc_total_price

@pytest.mark.parametrize("skus, expected_counts", [
    ("ABCDABAA", {'A':4, 'B':2, 'C':1, 'D':1}),
    ("ABE", -1),
    ("AAA", {'A':3})
])
def test_count_skus(skus, expected_counts):
    assert count_skus(skus) == expected_counts

@pytest.mark.parametrize("prices, special_offers, counts, expected_total", [
    ({'A': 50, 'B':30, 'C':20, 'D':15}, {'A':[(3, 130)], 'B':[(2, 45)]}, {'A':4, 'B':2, 'C':1, 'D':1}, 195),
    ({'A': 50, 'B':30, 'C':20, 'D':15}, {'A':[(3, 130)], 'B':[(2, 45)]}, {'A':3}, 130)
])
def test_calculate_total_price(prices, special_offers, counts, expected_total):
    assert calc_total_price(prices, special_offers, counts) == expected_total

@pytest.mark.parametrize("skus, expected_total", [
    ("ABCDABAA", 195),
    ("ABE", -1),
    ("AAA", 130)
])
def test_checkout(skus, expected_total):
    assert checkout(skus) == expected_total
