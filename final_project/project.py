def main():

    products = {}

    while True:
        try:
            item = input("New product name: ")
            cost = input(f"Introduce {item} cost: ")
            products[item] = cost
            print(f"El nuevo producto es {item} y su precio es {cost}")
        except EOFError: ## I can do this with a simple but very usefull if statement
            break
        else:
            print(products)
    else:
        products = products.pop(input())

    print(products)


def introduce_products_to_menu():
    ...


def delete_products_to_menu():
    ...



def function_three():
    ...









if __name__=="__main__":
    main()