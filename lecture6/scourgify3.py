import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    fn_ln_h = []
    with open(sys.argv[1]) as before:
        reader = csv.DictReader(before)
        for row in reader:
            last, first = row["name"].split(",")
            fn_ln_h.append({"first": first, "last": last, "house":row["house"]})
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

with open(sys.argv[2], "w") as after:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(after, fieldnames=fieldnames)
    writer.writeheader()
    for row in fn_ln_h:
        writer.writerow({"first": row["first"].strip(), "last": row["last"].strip(), "house": row["house"].strip()})

