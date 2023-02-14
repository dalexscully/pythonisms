# pylint: disable=import-error
import pytest

from linkedlist import LinkedList


# got help with this test from Daniel
def test_range():
    num_range = range(1,15+3)
    nums = LinkedList(num_range)
    assert len(nums) == 17


def test_for_in():
    fruits = LinkedList(('grapes', 'pommergranate', 'orange'))
    fruit_list = []
    for fruit in fruits:
        fruit_list.append(fruit)
    assert fruit_list == ['grapes', 'pommergranate', 'orange']


def test_list_comprehension():
    cars = LinkedList(('honda', 'ford', 'tesla'))
    cap_cars = [car.upper() for car in cars]
    assert cap_cars == ['HONDA ', 'FORD', 'TESLA']


def test_list_cast():
    rappers = ['lox', 'hov', 'drake']
    rapper = LinkedList(rappers)
    assert list(rapper) == rappers


def test_sum_values():
    ll_values = LinkedList((3,27,91))
    ll_total = 0
    for i in ll_values:
        ll_total += i
    assert ll_total == 121
