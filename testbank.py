import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
def test_hellothere():    
    assert value("hello there") == 0
def test_starthello():
    assert value("hello ahmed zulaikh") == 0
def test_starth():
    assert value("hi") == 20
def test_other():
    assert value("Good morning") == 100