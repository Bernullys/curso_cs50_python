import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")

elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")

else:
    adieu = p.join(names)
    print(f"Adieu, adieu, to {adieu}")
