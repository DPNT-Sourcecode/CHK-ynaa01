import pytest

from lib.solutions.CHK.checkout_solution import checkout, count_skus, calc_total_price

@pytest.mark.parametrize("skus, expected_counts", [
    ("ABCDABAA", {'A':4, 'B':2, 'C':1, 'D':1}),
    ("ABE", -1),
    ("AAA", {'A':3})
])
