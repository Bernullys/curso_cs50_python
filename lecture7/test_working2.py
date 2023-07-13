import pytest
from working2 import convert

def main():

    test_correct_format1()
    test_correct_format2()
    test_incorrect_format()
    test_out_of_range()

def test_correct_format1():
    assert convert("2 PM to 3 AM") == "14:00 to 03:00"
    
def test_correct_format2():
    assert convert("2:00 PM to 3:00 AM") == "14:00 to 03:00"

def test_incorrect_format():
    with pytest.raises(ValueError):
        convert("casa")

def test_out_of_range():
    with pytest.raises(ValueError):
        convert("3:60 AM to 4:70 PM")




if __name__ == "__main__":
    main()