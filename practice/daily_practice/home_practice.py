# inside help we can tye the function name and will print the optios the function has.
# Examples:
#help(print)
#help(range)
#help(sum)
#help(enumerate)

# Review map

fruit = ["orange", "apple", "pine", "banana"]
fruits = map(len, fruit)
fruits = map(lambda x: x + "s", fruit)
print(list(fruits))

# Review filter

six_letters_fruits = filter(lambda x: len(x) >= 6, fruit)
print(list(six_letters_fruits))

# Review sorted

num = list(range(15))
sorted_num = sorted(num, reverse=True)
print(sorted_num)

people = [
    {"name": "Ber", "age": 37},
    {"name": "Alice", "age": 30},
    {"name": "Pat", "age": 34}
]
sorted_people = sorted(people, key= lambda person: person["name"], reverse=True )
print(list(sorted_people))


# Review enumerate

counting_people = enumerate(people)
for indx, person in counting_people:
    print(indx, person)


# Review zip

# This is how we can put together a couple of lists:
names = ["Ber", "Pat", "Joy", "Alice"]
ages = [37, 34, 7]
for indx in range(min(len(names), len(ages))):  # min function is to ensure the loop uses the minimum equal amount of itiems of each list. 
    name = names[indx]
    age = ages[indx]
    print(f"{name} is {age} years old")

# Now using zip
# Also can add more lists:
genders = ["Male", "Female", "Male", "Female"]
combining = zip(names, ages, genders)
for name, age, gender in combining:
    print(f"{name} is {age} years old, and is a {gender}")