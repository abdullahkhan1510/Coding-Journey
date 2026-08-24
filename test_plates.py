import pytest
from plates import is_valid

def test_valid():
    assert is_valid("AB123") == True
def test_length():
    assert is_valid("a") == False
    assert is_valid("AAAAA2222") == False
def test_nums():
    assert is_valid("AB012") == False
    assert is_valid("AB2121") == True
def test_punc():
    assert is_valid("ab!23") == False
