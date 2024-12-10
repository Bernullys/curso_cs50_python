# inside help we can tye the function name and will print the optios the function has.
# Examples:
#help(print)
#help(range)
#help(sum)

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

sorted_people = sorted(people, key= lambda person: person["name"] )

print(list(sorted_people))