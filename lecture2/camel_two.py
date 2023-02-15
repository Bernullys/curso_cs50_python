

camelCase = input("camelCase: ")

snake_case_store = ""

for letter in camelCase:
    if letter.isupper() == True:
        snake_case_store = snake_case_store + "_" + letter.lower()
    else:
        snake_case_store = snake_case_store + letter

print(snake_case_store)

