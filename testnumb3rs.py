from week7 import validate
def test_valid():
    assert validate("222.222.222.222") == True
    assert validate("1.2.3.4") == True
    assert validate("212.45.78.115") == True
def test_invalid():
    assert validate("999.999.999") == False
    assert validate("-1.4.982.2") == False
    assert validate("Cat") == False