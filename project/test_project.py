import pytest
from project import selection, open_csv_to_read, show_table_in_terminal, checking_existing_customer, add_items_to_customer, add_items_to_menu, delete_product_to_menu, add_stock, checking_intenger

def main():

    test_selection()


def test_selection():
    assert selection() == "1" 






if __name__ == "__main__":
    main()