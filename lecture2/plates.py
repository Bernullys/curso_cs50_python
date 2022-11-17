plate = input("Plate: ")

abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

first_two = plate[0:2]

print(first_two)

for two_first_letters in first_two:

    if two_first_letters in abc:
        valid = True
        print(valid)
        break

plate_length = len(plate)

print(plate_length)

if 2 <= plate_length <= 6:
    print("OKOK")
else:
    print("OH NOO")






