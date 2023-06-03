import pytest
from numb3rs import validate

def main():

    test_correct_ip()
    test_incorrect_ip()

def test_correct_ip():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255")

def test_incorrect_ip():
    assert validate("1.1.1.256") == False
    assert validate("cat") == False
    assert validate("1..1.1.1") == False



if __name__=="__main__":
    main()