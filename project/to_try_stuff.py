import csv
import time

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


print("#######################################################################")

# custumer_name = "Bernardo"
# item = "Soda"
# price = 12

# with open ("../current_bills.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["custumer_name", "item", "price"])
#     writer.writeheader()
#     writer.writerow({"custumer_name": custumer_name, "item": item, "price": price})

print("##################################################################################")

actual_time = time.asctime()

print(actual_time)


def open_csv_read (csv_file):
    list_products = []
    with open(csv_file, "r", newline="") as file:
        info = csv.reader(file)
        print(info)
        for row in info:
            list_products.append(row)
        print(list_products)
        # for row in info:
        #     check_item = "Fries"
        #     if row["item"] == check_item:
        #         print("Item exists already")
        #     print(row)


#open_csv_read("./menu.csv")  