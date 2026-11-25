from app import greet


def test_greet():
    assert greet("MacBook") == "Hello, MacBook!"
