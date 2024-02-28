menu_optional = {
    "fries": 12,
    "soda": 6,
    "hog_dog": 8
}

menu_optional_two = [
    {"item": "burger",
     "price": 13
     },
    {"item": "soda",
     "price": 3
     }
]

print(menu_optional["fries"])

print("##########################################")

for me in menu_optional_two:
    print(me["price"])
    print(menu_optional_two[1]["item"])