import pytest
from um2 import count

def main():

    test_uppers()
    test_puntuations()
    test_overlaping()


def test_uppers():
    assert count("UM") == 1


def test_puntuations():
    assert count("um.") == 1

def test_overlaping():
    assert count("album") == 0




if __name__ == "__main__":
    main()