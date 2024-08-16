import pytest
from bill import Bill
import csv
from project import selection, open_csv_to_read, show_table_in_terminal, checking_existing_customer, add_items_to_customer, add_items_to_menu, delete_product_to_menu, add_stock, checking_intenger

def main():


    test_selection()
    test_checking_existing_customer()


def test_selection():
    assert selection("0") == "0"
    assert selection("1") == "1"
    assert selection("2") == "2"
    assert selection("3") == "3"
    assert selection("4") == "4"
    assert selection("5") == "5"
    assert selection("6") == "6"
    assert selection("7") == "7"
    assert selection("8") == "8"
    assert selection("9") == "9"
    assert selection("10") == "10"
    assert selection("11") == "11"
    with pytest.raises(ValueError):
        selection("12")
    with pytest.raises(ValueError):
        selection("!!")
    with pytest.raises(ValueError):
        selection("house")

def test_checking_existing_customer():

    customer1 = Bill("Bernardo")
    customer2 = Bill("Patricia")
    customers = [customer1, customer2]
    any_ustomers = []

    assert checking_existing_customer("Bernardo", customers) == ("Bernardo", 0)
    assert checking_existing_customer("Patricia", customers) == ("Patricia", 1)
    assert checking_existing_customer("12345", customers) == (False, False)
    assert checking_existing_customer("Bernardo", any_ustomers) == (False, False)

def test_open_csv_to_read(tmpdir):

    csv_file = tmpdir.join("test_file.csv")
    with open(csv_file, "w", newline="") as data:
        writer = csv.DictWriter(data, fieldnames = ["column1", "column2", "column3"])
        writer.writeheader()
        writer.writerow({"column1": "value1", "column2": "value2", "column3": "value3"})

    
    temporaly_file = open_csv_to_read(csv_file)
    expected_result = [{"column1": "value1", "column2": "value2", "column3": "value3"}]

    assert temporaly_file == expected_result





if __name__ == "__main__":
    main()