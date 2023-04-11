from fuel import convert,gauge
import pytest

def main():
    
    test_zero_division()
    test_value_error()
    test_input()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("Dog/cat")

def test_input():
    assert convert("1/4") == 0.25 and gauge(0.25) == "25%"
    assert convert("1/100") == 0.01 and gauge(0.01) == "E"
    assert convert("1/1") == 1 and gauge(1) == "F"


if __name__ == "__main__":
    main()