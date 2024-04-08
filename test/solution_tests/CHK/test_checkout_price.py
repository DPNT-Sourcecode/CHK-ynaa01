import pytest

from lib.solutions.CHK.checkout_solution import checkout


def test_checkout_valid_input():
    assert checkout("E") == 40
    assert checkout("ABCDE") == 155
    assert  checkout("AAAAA") == 200
    assert checkout("EE") == 80
    assert checkout("EEB") == 80
    assert checkout("EEEB") == 120


def test_checkout_invalid_input():
    assert checkout("X") == -1
    assert checkout("") == 0
    assert checkout("ABABABABAY") == -1


