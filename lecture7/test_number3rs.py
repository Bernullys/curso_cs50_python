import pytest
from numb3rs import validate

def main():
    
    test_out_of_range()
    test_under_range()
    test_without_one()
    test_with_zeros()
    test_more_dots()

def test_out_of_range():

    assert validate("256.123.123.12") == False
    assert validate("-5.123.123.12") == False
    assert validate(".123.123.12") == False
    assert validate("00.123.123.12") == False
    assert validate("0..123.123.12") == False
    assert validate("255.255.255.255") == True

if __name__=="__main__":
    main()
