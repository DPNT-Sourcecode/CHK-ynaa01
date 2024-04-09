import pytest

from lib.solutions.CHK.checkout_solution import checkout

valid_test_data = [
    ("E", 40),
    ("ABCDE", 155),
    ("AAAAA", 200),
    ("EE", 80),
    ("EEB", 80),
    ("EEEB", 120),
    ("AAA", 130),
    ("AAAA", 180),
    ("AAAAAAAA", 330),
    ("AAAAAA", 250),
    ("AAAAAAA", 300),
    ('F',10),
    ('ABCDEF', 165),
    ('HHHHHHHHH', 85),
    ('HHHHHHHHHH', 80),
    ('KKK', 190),
    ('NNNM', 120),
    ('NNN', 120),
    ('PPPPPP', 250),
    ('QQQQ', 110),
    ('RRRQ', 150),
    ('UUUUUUUU', 240),
    ('VVVVVVVVVVV', 480),
    ('XXX', 45),
    ('XXXZ', 62),
    ('S', 20),
    ('ZZZZY', 86),
    ('K', 70),
    ('ABCDEFGHIJKLMNOPQRSTUVW', 795)
]

@pytest.mark.parametrize("input_str, expected_output", valid_test_data)
def test_checkout_valid_input(input_str, expected_output):
    assert checkout(input_str) == expected_output


def test_checkout_invalid_input():
    assert checkout("s") == -1
    assert checkout("") == 0
    assert checkout("ABABABABaAY") == -1





