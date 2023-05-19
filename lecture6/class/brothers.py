import csv

name = input("What's your name? ")
city = input("Where's your home? ")

with open("brothers.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writerow({"name": name, "city": city})