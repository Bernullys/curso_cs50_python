import pytest
from working import convert

def main():

    test_am_pm()
    test_wrong_time()


def test_am_pm():
    assert convert("12 AM to 12 PM") == "00:00 to 24:00"





if __name__=="__main__":
    main()