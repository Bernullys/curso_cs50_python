import pytest
from plates import is_valid

def main():

    test_first_two()
    test_len()
    test_puntuation()
    test_numbers()

def test_first_two():
    assert is_valid ("AS") == True
    assert is_valid ("A2") == False

def test_len():
    assert is_valid("ASDSAA") == True
    assert is_valid("A") == False
    assert is_valid("DJDJDJD") == False
    assert is_valid("ABC123") == True

def test_puntuation():
    assert is_valid("A!..A") == False
    assert is_valid("ASD?3") == False

def test_numbers():
    assert is_valid("23ASS") == False
    assert is_valid("AS012") == False
    assert is_valid("ASW456") == True
    assert is_valid("AS5AS") == False


if __name__ == "__main__":
    main()