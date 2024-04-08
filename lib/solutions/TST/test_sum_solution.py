import pytest

from lib.solutions.SUM.sum_solution import SumSolution

@pytest.fixture()
def sum_fixture():
    return SumSolution()

def test_sum_solution(sum_fixture):
    assert sum_fixture.compute(1, 5) == 6