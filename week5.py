import pytest
from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten ("AEIOU") == ""
    assert shorten ("Abdu") == "bd"
    assert shorten("CS50P") == "CS50P"
    
