import pytest
from bank import value

def main():

    test_hello()
    test_hey()
    test__hey()
    test_whatsup()
    test_HELLO()
 

def test_hello():
    assert value("hello") == 0

def test_hey():
    assert value("hey") == 20

def test__hey():
    assert value("   hey") == 20

def test_whatsup():
    assert value("whatsup") == 100

def test_HELLO():
    assert value("HELLO") == 0


if __name__=="__main__":
    main()