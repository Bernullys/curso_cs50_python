items = []
while True:
    try:
        item = input("").upper()
    except EOFError:
        break
    else:
        items.append(item)
items_dict = {}
for i in items:
    if i in items_dict:
        items_dict[i] += 1              # items_dict[i] are the keys
    else:
        items_dict[i] = 1

for n in sorted(items_dict):
    print(f"{items_dict[n]} {n}")      #  items_dict[n] are the values

