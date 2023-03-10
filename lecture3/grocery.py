grocerys = {}
while True:
    try:
        item = input("").upper()
    except EOFError:
        break
    if item in grocerys:
        grocerys[item] += 1
    else:
        grocerys[item] = 1

for items in sorted(grocerys):
    print(grocerys[items], items)
