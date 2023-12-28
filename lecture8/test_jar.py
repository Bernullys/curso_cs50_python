import pytest
from jar2 import Jar

def main():

    test_init()
    test_str()


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5) == 5


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)



if __name__=="__main__":
    main()