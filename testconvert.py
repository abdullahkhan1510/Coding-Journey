import pytest
from convert import convert

def test_zero():
    assert(convert(0)) == 32
def test_hundred():
    assert(convert(100)) == 212
def test_neg():
    assert(convert(-40)) == -40