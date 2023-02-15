
# This code has a big bug because it only works for a simple camelCase

def main():

    variable_name = input("camelCase: ")

    name_snake_case = convert_name_camelCase_to_snake_case(variable_name)

    print(f"snake_case: {name_snake_case}")

    return name_snake_case

    print(f"snake_case: {res}")

def convert_name_camelCase_to_snake_case(camel_case_name):

    if camel_case_name.islower() == True:
        return camel_case_name

    for letter in camel_case_name:
        if letter.isupper() == True:
            a, b = camel_case_name.split(letter)

            c = a + "_" + letter.lower() + b

            return c

res = main()


