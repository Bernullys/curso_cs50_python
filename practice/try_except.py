menu = ["fries", "sandwich", "cheeseburger", "coffee", "soda"]

try:
    item = int(input())
    if item not in range(len(menu)):
        raise ValueError ("Item not found")

except (ValueError):
    print("Item not found")
else:
    print(menu[item])
    print("Thanks for your order")

