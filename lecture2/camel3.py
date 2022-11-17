def main():

    variableInCamelCase = input("camelCase: ")

    variable_in_snake_case = change_from_CC_to_sc(variableInCamelCase)

    store_letter = print(f"snake_case: {variable_in_snake_case}")


def change_from_CC_to_sc(variableInCamelCase):

    store_letter = ""

    for letterOfVariableInCamelCase in variableInCamelCase:
        if letterOfVariableInCamelCase.isupper() == True:
            if len(store_letter) > 0:
                store_letter += "_" + letterOfVariableInCamelCase.lower()
            else:
                store_letter += letterOfVariableInCamelCase.lower()
        else:
            store_letter += letterOfVariableInCamelCase.lower()
    
    return store_letter

main()