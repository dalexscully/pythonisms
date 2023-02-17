from pythonism import MyCollection
import pytest


def test_str(my_collection):
    assert str(my_collection) == "[1, 2, 3, 4, 5]"


def test_len(my_collection):
    assert len(my_collection) == 5


def test_getitem(my_collection):
    assert my_collection[2] == 3


def test_contains_true(my_collection):
    assert 3 in my_collection


def test_contains_false(my_collection):
    assert 6 not in my_collection


def test_reversed(my_collection):
    reversed_collection = reversed(my_collection)
    assert list(reversed_collection) == [5, 4, 3, 2, 1]


@pytest.fixture
def my_collection():
    return MyCollection([1, 2, 3, 4, 5])