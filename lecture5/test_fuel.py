import pytest
from fuel import convert, gauge

def main():

    test_entry()
    test_correct_gauge()

def test_entry():
    assert convert("2/5") == 40
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("8/5")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_correct_gauge():
    assert gauge(40) == f"{40}%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

if __name__=="__main__":
    main()