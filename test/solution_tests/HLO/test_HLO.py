import pytest

from lib.solutions.HLO.hello_solution import HelloFriend

@pytest.fixture()
def hello_friend_fixture():
    return HelloFriend()

def test_hello_friend(hello_friend_fixture):
    assert hello_friend_fixture.hello("James") == "Hello, James!"