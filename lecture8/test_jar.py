import pytest
from jar2 import Jar

def main():

    test_init()
    test_str()


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(5) == "🍪🍪🍪🍪🍪"


def test_withdraw():
    ...



if __name__=="__main__":
    main()