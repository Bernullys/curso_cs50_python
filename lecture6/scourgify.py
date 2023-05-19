#expects the user to provide two command-line arguments:
#first: the name of an existing csv file to read as input, whose columns oreder are complete_name,house
#second: the name of a new csv file to write as output, whose columns order are first,last,house
#the entry has to provide exactly two command-line arguments

import sys
import csv
from lines2 import exact_input

# full_names = []
# houses = []
name_last_house = []
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        separated_name = row["name"].split(",")
        name_last_house.append({"first_name": separated_name[1], "last_name": separated_name[0], "house": row["house"]})
    # for row in reader:
    #     full_names.append(row['name'])
    #     houses.append(row['house'])

# first_names = []
# last_names = []
# for names in full_names:
#     last_name, first_name = names.split(",")
#     first_names.append(first_name)
#     last_names.append(last_name)

with open(sys.argv[2], 'w') as file:
    fieldnames = ['first_name', 'last_name', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    #writer.writerow({"first_name": "first_name", "last_name": "last_name", "house": "house"})
    writer.writeheader()

    for row in name_last_house:
        writer.writerow({"first_name": row["first_name"], "last_name": row["last_name"], "house": row["house"]})