from cuenta import Tap

def main():

    products = {
        "Burger": "$5",
        "Pizza": "$8",
        "Fries": "$3",
        "Drink": "$2",
    }

    introduce_products = input("Do you want to intruduce new products? ")
    afirmative = ["yes", "y", "YES", "Y"]
    if introduce_products in afirmative:
        products = {**products, **introduce_products_to_menu()}

    print(products)

    delete_products_from_menu = input("Do you want to delete products from the menu? ")
    if delete_products_from_menu in afirmative:
        delete_products_to_menu(products)
     
    print(products)


def introduce_products_to_menu():
    new_products = int(input("How many products do you want to introduce to the bar? "))
    new_products_base = {}
    amount_of_products = 0
    while amount_of_products < new_products:
        new_product = input("New product name: ")
        new_product_cost = input(f"{new_product} cost: ")
        new_products_base[new_product] = f"${new_product_cost}"
        amount_of_products += 1
    return new_products_base


def delete_products_to_menu(menu_products):
    delete_products = int(input("How many products do you want to delete? "))
    amount_of_products = 0
    while amount_of_products < delete_products:
        delete_product = input("Witch product do you want to delete? ")
        new_products_base = menu_products.pop(delete_product)
        amount_of_products += 1
    return  new_products_base



def function_three():
    ...


bernard = Tap()
bernard.consumption("Fries")
bernard.consumption("Burger")
bernard.bill(10, 10)








if __name__=="__main__":
    main()