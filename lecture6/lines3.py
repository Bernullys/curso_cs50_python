import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

try:
    count = 0
    with open (sys.argv[1]) as file:
        for line in file:
            striped_line = line.lstrip()
            if striped_line == "":
                count = count
            elif striped_line.startswith("#"):
                count = count
            else:
                count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

else:
    print(count)