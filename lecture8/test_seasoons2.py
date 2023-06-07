import pytest
from seasons2 import right_format_input, formating_date

def main():

    test_formating_date()
    test_input_date_format()


def test_formating_date():
    assert formating_date("2019-01-01") == (2019, 1, 1)


def test_input_date_format():
    assert right_format_input("1999-01-01") == "1999-01-01"




if __name__=="__main__":
    main()