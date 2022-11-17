def main():

    variable_name = input("camelCase: ")

    name_snake_case = convert_name_camelCase_to_snake_case(variable_name)

    #print(f"snake_case: {name_snake_case}") // SI ES QUE NO LO PONGO A IMPRIMIR COMO ESTA ABAJO AL FINAL

    return name_snake_case

def convert_name_camelCase_to_snake_case(camel_case_name):

    if camel_case_name.islower() == True:
        return camel_case_name

    store_name = ""
    #start_underscore = False  // NO LO NECESITO

    for letter in camel_case_name:

        if letter.isupper() == True:

            if len(store_name) > 0:
                #store_name = store_name + letter.lower()
                store_name += "_" + letter.lower()
            else:
                store_name += letter.lower()

        else:
            store_name += letter.lower()

    return store_name


res = main()

print(f"snake_case: {res}")
