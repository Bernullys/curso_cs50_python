from plates import is_valid

def main():

    test_first_two()



def test_first_two():

    assert is_valid("ar") == True
    assert is_valid("12") == False





if __name__ == "__main__":
    main()