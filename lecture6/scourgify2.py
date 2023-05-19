import sys
import csv
from lines2 import exact_input

exact_input()

name_last_name_house = []
with open(sys.argv[1]) as file_to_read:
    reader = csv.DictReader(file_to_read)
    for each_row in reader:
        separated_names = each_row["name"].split(",")
        name_last_name_house.append({"name": separated_names[1], "last_name": separated_names[0], "house": each_row["house"]})

with open(sys.argv[2], "w") as file_to_write:
    fieldnames = ["name", "last_name", "house"]
    writer = csv.DictWriter(file_to_write, fieldnames = fieldnames)
    writer.writeheader()

    for each_row in name_last_name_house:
        writer.writerow({"name": each_row["name"], "last_name": each_row["last_name"], "house": each_row["house"]})


