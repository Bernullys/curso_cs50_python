import pytest
from twttr import shorten

def main():

    test_upper_vowels()
    test_lower_vowels()
    test_numbers()
    test_puntuations()


def test_upper_vowels():
    assert shorten("HELLOAIU") == "HLL"

def test_lower_vowels():
    assert shorten("Bernardo1") == "Brnrd1"

def test_numbers():
    assert shorten("12345Br") == "12345Br"

def test_puntuations():
    assert shorten("Bern.Davila!") == "Brn.Dvl!"

if __name__=="__main__":
    main()