import pytest
from refuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("-1/4")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(10) == "10%"