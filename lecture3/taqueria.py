
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0
while True:
    try:
        order = input("Item: ")
        for entrees in menu:
            if  entrees.casefold() == order.casefold():
                cost += menu[entrees]
                #print(f"Total: ${cost}0")
                print("Total: $",f"{cost:.2f}",sep="")
            else: pass
    except EOFError:
        print("\n")
        break