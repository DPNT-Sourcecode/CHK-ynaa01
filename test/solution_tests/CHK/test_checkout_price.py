import pytest

from lib.solutions.CHK.checkout_solution import checkout


def test_checkout_valid_input():
    assert checkout("ABCDABAA") == 260
    assert checkout("AAA") == 130
    assert checkout("C") == 20

def test_checkout_invalid_input():
    assert checkout("E") == -1
    assert checkout("") == 0
    assert checkout("ABABABABAY") == -1