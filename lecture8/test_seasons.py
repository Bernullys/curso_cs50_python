import pytest
from seasons import validate_date, split_date_format

def main():

    test_date_format()

def test_date_format():

    assert validate_date("1999-01-01") == "1999-01-01"
    assert validate_date("cualquiercosa") == ("Invalid date")







if __name__=="__main__":
    main()