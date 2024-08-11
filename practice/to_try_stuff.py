import csv
import time
import re

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

just_a_list = ["Bernardo", "Patricia"]

#print(just_a_list.index("Bernardo"))
#print(len(just_a_list))


#print(menu_optional["fries"])

#print("##########################################")

for me in menu_optional_two:
    print(me["price"])
    print(menu_optional_two[1]["item"])


#print("#######################################################################")

# custumer_name = "Bernardo"
# item = "Soda"
# price = 12

# with open ("../current_bills.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["custumer_name", "item", "price"])
#     writer.writeheader()
#     writer.writerow({"custumer_name": custumer_name, "item": item, "price": price})

#print("##################################################################################")

actual_time = time.asctime()

#print(actual_time)


def open_csv_read (csv_file):
    list_products = []
    with open(csv_file, "r", newline="") as file:
        info = list(csv.DictReader(file))
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

# I need a function which returns always a variable tha contains a DictReader so I can manipulate that info in diferents ways.

from tabulate import tabulate
# List of dictionaries with three key-value pairs
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Extract only the columns you want (name and age)
filtered_data = [{k: v for k, v in d.items() if k in ["name", "age"]} for d in data]

# Create the table with the filtered columns
table = tabulate(filtered_data, headers="keys", tablefmt="grid")

# Print the table
#print(table)

print("#############################################################################")

with open("./countries.csv") as file:
    reader = list(csv.reader(file))
    for row in reader:
        print(row)

new_title_list = ["first", "second", "third", "fourd"]

reader.insert(0, new_title_list)

for m in reader:
    print(m)