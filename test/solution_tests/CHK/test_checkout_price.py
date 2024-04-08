import pytest

from lib.solutions.CHK.checkout_solution import checkout


def test_checkout_valid_input():
    assert checkout("E") == 40
    assert checkout("ABCDE") == 155

def test_checkout_invalid_input():
    assert checkout("X") == -1
    assert checkout("") == 0
    assert checkout("ABABABABAY") == -1

# def test_checkout_special_offer_e():
#     assert checkout("AAABBEEE") == 245