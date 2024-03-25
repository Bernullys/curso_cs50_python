
# This code has a big bug because it only works for a simple camelCase

def main():

    variable_name = input("camelCase: ")

    name_snake_case = convert_name_camelCase_to_snake_case(variable_name)

    print(f"snake_case: {name_snake_case}")

    return name_snake_case

    print(f"snake_case: {res}")

def convert_name_camelCase_to_snake_case(camel_case_name):

    sanake_kase = ""

    for letter in camel_case_name:
        if letter.isupper() == True:
            if len(sanake_kase) > 0:
                to_lower = letter.lower()
                sanake_kase += "_" + to_lower
            else:
                sanake_kase += letter.lower()
        else:
            sanake_kase += letter.lower()

    return sanake_kase

res = main()


