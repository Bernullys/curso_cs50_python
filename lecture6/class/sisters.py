import csv

sisters = []

with open("sisters.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sisters.append({"name": row["sister"], "country": row["country"]})

for sister in sorted(sisters, key=lambda sister: sister["name"]):
    print(f"{sister['name']} is in {sister['country']}")