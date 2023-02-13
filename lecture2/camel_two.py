

camelCase = input("camelCase: ")


uppers = ["A", "B", "C", "D"]

for i in camelCase:
    if i in uppers:
        i = "_",i.lower()
    print(i, end="")

