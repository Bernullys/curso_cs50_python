from bank import value

def main():

    test_value_with_numbers()
    test_value_with_uppers()
    test_value_with_lowers()

def test_value_with_numbers():

    assert value("123Hello") == "100"
    assert value("Whats up") == "100"
    assert value("OH hwy you") == "100"

def test_value_with_uppers():

    assert value("HELLO") == "0"

def test_value_with_lowers():

    assert value("hey") == "20"

if __name__=="__main__":
    main()
