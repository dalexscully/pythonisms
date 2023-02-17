from linkedlist import LinkedList
import pytest


@pytest.fixture
def multiple_item_list():
    return LinkedList([1, 2, 3, 4])


def test_init_with_multiple_items(multiple_item_list):
    assert len(multiple_item_list) == 4
    assert multiple_item_list.head.value == 1


def test_str_with_multiple_items(multiple_item_list):
    assert str(multiple_item_list) == "[ 1 ] -> [ 2 ] -> [ 3 ] -> [ 4 ] -> None"


def test_insert(multiple_item_list):
    multiple_item_list.insert(1)
    assert str(multiple_item_list) == "[ 1 ] -> [ 1 ] -> [ 2 ] -> [ 3 ] -> [ 4 ] -> None"


def test_iter(multiple_item_list):
    assert list(iter(multiple_item_list)) == [1, 2, 3, 4]


def test_len(multiple_item_list):
    assert len(multiple_item_list) == 4


def test_eq(multiple_item_list):
    assert multiple_item_list == LinkedList([1, 2, 3, 4])


def test_getitem(multiple_item_list):
    assert multiple_item_list[0] == 1
    assert multiple_item_list[1] == 2
    assert multiple_item_list[2] == 3
    assert multiple_item_list[3] == 4
    with pytest.raises(IndexError):
        multiple_item_list[-1]
    with pytest.raises(IndexError):
        multiple_item_list[4]
