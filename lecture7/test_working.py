import pytest
from working import convert

def main():

    test_am_pm()
    test_wrong_format()


def test_am_pm():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_wrong_format():
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")



if __name__=="__main__":
    main()