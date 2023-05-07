# curso_cs50_python
I'm going to put here notes of every clase and exercice of this course

```py

    print()
    print("\n")                             #Imprime una linea vacia
    print(end="")                           #Imprime y termina de una vez
    print(sep="")                           #esto imprime una separacion con el caracter que definamos - usable con dicts 
    print(var\n *3, sep="character")        #esto imprimira tres veces la variable enla misma linea separada por un caracter
    
    print("hello, "friend"")                #arroja error
    print("hello, \"friend\"")              #esto solucionaria -- el backslash siempre rompe el significado del caracter en este lenguaje
    print("hello, 'friend'")                #esto seria otra solucion pero menos usada

    print(f"str ${variable}")               #str que queramos
    print(f"{number:,})                     #print a number with 1,000 format
    print(f"{float:.nf})                    #print a float with n decimals

    input()
    int()
    float()
    round(number,n)                         #round to n decimals       
    pow(x,n)                                #returns the power of x to the n

    def main():
    def function():
    return
    funtion()
    if__name__=="__main__":
        main()

    abs()                                       # retorna el valor absoluto de un numero
    len()                                       # returns the length of the variable or list
    sorted()                                    #ordena en orden alfabetico
    .append()                                   #is used with a for loop to make a list or in the right way to make a dict

Methods:

    str.strip()                             #remove whitespace from the str
    str.rstrip()
    str.title()                             #capitalize the first letter of each word
    str.lower()
    str.casefold()
    str.replace("lo_que_sea", "por_otra_cosa_que_sea")
    var1, var2 = varx.split(":") //de una variable con una entrada dividida por un caracter los separa desde donde se ponga el caracter
    str.startswith()
    str.endswith()
    str.isupper()                               #returns True or False if the str is upper
    str.islower()                               #returns True or False if the str is lower
    str.isdigt()                                #entrega True or False si el que el str contiene solo digitos no simbolos o puntuación.
    str.index()                                 #entrega el indice de la letra del string - la letra va dentro de los parentesis con comillas
    str.isalpha()
    str.isalnum()
    str.removeprefix()                          #remove the begginning of a string

Shortcuts:

    windows + .                                 #window of emojis 👌
    ctrl + d                                    #send a EOFError
    ctrl + c                                    #stop runing the code

Math Operators:

    + - * / %

    +=
    -=

Conditionals Operators:

    <
    >
    <=
    >=
    ==
    !=
    ===

Conditionals:

    if condition or condition2:
    if condition | condition2:
    if condition and condition2:
    if condition & condition2:
    elif condition:
    else:
    match variable:
        case option1 | option2:
            code
        case option_x:
            code2
        .
        .
        .

Loops:


    while condition :

    whille condition :
        continue
        break

    for condition:                              # for loops iterates through a list of items

    range(n)                                    # provides back n values


    NOTA: me di cuenta de que si en una funcion se regresa solo True o solo False siempre se regresara ese booleano asi la condicion no se cumpla.
    Por otro lado tengo que tener presente de que si se quiere probar varias condiciones, se pueden probar las condiciones falsas menos una.


Lists:

    var_lists = [0, 1, 2, ..., n]               # list are the equivalent of arrays in javascript

    if variable in var_lists:
        check if the variable is in the list

    if variable not in var_lists:
        check if the variable is not in the list

Dicts:

    dict or dictionaries are a data structure that allows you to associete keys with values

        var_dict = {                            # la parte de varn son las keys y la parte de las Varn.n son los valores de las keys - Un valor puede ser None
        "key1": "value1",
        "key_n": value_N,
        .
        .
        .
    }
    for var in var_dict:
        print(var, var_dict[var])               #Esto imprimira key value


    var_dict = [                                # esto es un list of dicts - Un valor puede ser None
        {var1: Var1.1, varX: VarX.1, ...}
        {var2: Var2.2, varY: VarY.1, ...}
        ...
        {varn: Varn.n, varN: VarN.1, ...}
    ]

    for var in var_dict:
        print(var[var1], var[varX], var[varX.1], sep=", ")       # Esto imprimiria las keys con sus valores deparados por coma y espacio

    at grocery.py in lecture3 is how to create a dict and how to print it

Slices:

    str[n:]
    str[0:n]
    list[0:n]


Exceptions:

    try:
        code...
    except AnyError:
        code... or pass
    else:
        code...


    while True:                                                  #Some convinations
        try:
            code
        except (error_type_1, ..., error_typy_n)
            code
            or
            try:
                code
                ...
                break
                else:pass                                        # this will promp again for an input
        except (error_type_1, ..., error_typy_n)
            try:
                code
                else:pass
            except (error_type)
                pass
        

Libraries or Modules in Python: Always check the documents to know how the specific module works

#Always check its functions with chatgpt

    import random
    random.choice([list])
    random.randint(int1, int2)
    random.shuffle([list])                              #shuffle a list into a random order

    import statistics
    statistics.men([list of numbers])                   #average of these values

    import sys
    sys.argv[n]
    sys.exit("string")

    pip                                                 #package manager
    pip install name_of_package
    
    import requests                                     #to use APIs
    variablex = requests.get("API link")
    variablex.json()                                    #this got the API info and returns a dict

    variablex["list1"]["list2"]...["listn"]             #until get the value we want

    import json
    json.dumps(variablex.json(), indent=2)              #to make the output more readable

    import inflect
    p = inflect.engine()                                #this to lines come together

    import emoji
    emoji.emojze(str)

    from pyyfiglet import Figlet
    figlet = Figlet()                                   #this two come together

    from tabulate import tabulate

    import csv

    from PIL import Image, ImageOps
    Image.open()
    size =imagex.size
    ImageOps.fit(imagex, size)
    imagex.paste(imagey, imagey)
    imagex.save(file_name_with_extension)

    import os                                           
    os.path.splitext()                                  #split from extensions

    import re
    re.search(pattern, string, flags=0)
    re.match
    re.fullmatch

    import validators             #to validate specifics inputs

Unit Test:

    pytest                                              #is a installed package
    pytest file_name                                    #to run the test
    test_file_name                                      #has to be the name of the file with the test

    this is how is used:

    from file import name_of_function_under_test1, name_of_function_under_testn
    import pytest
    def main():
        function_test_name1()
        function_test_namen_or_excetion()
    def function_test_name1():
        assert name_of_function_under_test1(corner argument) == correct_output and name_of_function_under_testn(corner argument) == correct_output
    def function_test_namen_or_excetion():
        with pytest.raises(ErrorException):
            name_of_function_under_testn(error argument)
    if __name__"__main__":
        main()


File I/O:

    open("file_name.extension", "w")
    .write()
    .close()
    open("file_name.extension", "a")
    open("file_name.extension", "r")

    with open("file_name.extension", "a") as file_name:
        file_name.write()

    with open("file_name.extension", "r") as file_name:
        lines = file_name.readlines()
    for line in lines:
        print(line.rstrip())

    Example:
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    def get_name(student):
        return student["name"]
    for student in sorted(students, key=get_name):
        print(f"{student['name']} is in {student['house']}")

    Same same example:
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")
            students.append({"name": name, "house": house})
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")

    Example:
    import csv
    students = []
    with open("students.csv") as file:
        reader = csv.reader(file)                                               #returns a list
        for row in reader:
            students.append({"name": row[0], "home": row[1]})
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")

    Example:
    import csv
    students = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)                                           #returns a dict
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['home']}")

    Example:
    import csv
    name = input("What's your name? ")
    home = input("Where's your home? ")
    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writeheader()
        writer.writerow({"name": name, "home": home})

    Example:
    name_last_house = []
    with open(sys.argv[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            separated_name = row["name"].split(",")
            name_last_house.append({"first_name": separated_name[1], "last_name": separated_name[0], "house": row["house"]})
    with open(sys.argv[2], 'w') as file:
        fieldnames = ['first_name', 'last_name', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in name_last_house:
            writer.writerow({"first_name": row["first_name"], "last_name": row["last_name"], "house": row["house"]})


Regular Expressions:

    import re
    re.search(pattern, string, flags=0)

            #Use this page to check the patter we are going to check first regex101.com
            #these ones look afther their own position:
    .       #any character except a new line
    *       #0 or more repetitions
    +       #1 or more repetitions
    ?       #0 or 1 repetition
    {m}     #m repetitions
    {m,n}   #m-n repetitions

    \                   #backslash is a scape character
    r                   #in front of a string is a row string r"str" none character in tha string is special
    ^                   #matches the start of the string
    $                   #matches the end of the string
    []                  #set of characters
    [^]                 #complementing the set - [^x]+ --- this means any character except X
    [a-zA-Z0-9_]        #a to z and A to Z and 0 to 9 and _
    \w                  #means the same as [a-zA-Z0-9_]
    \d                  #decimal digit
    \D                  #not a decimal digit
    \s                  #whitespace characters
    \S                  #not a whitespace character
    \w                  #word character, as well as numbers and the underscore
    \W                  #not a word character
    |                   #or

    A|B                 #either A or B
    (...)               #a group
    (?:...)             #non-capturing version

                        #built in flag cariables:
    re.IGNORECASE       #ignore if is upper or lower case
    re.MULTILINE
    re.DOTALL
                        #cleaning up user input
    matches.groups()    #returns specific groups
    matches.group()     #returns specific group
    :=                  #warlus operator assigns a value from right to left and allows to ask a boolean question at the same time

                        #extracting user input
    re.sub(pattern, repl, string, count=0, flags=0)
    
    ?:                  #tells the compiler it does not have to capture what is in that spot in our regular expression
    \b                  #bunaries

    #Always separed with groups. Use or |
    #look out for patrons
    #working is a good problem to keep it in mind
    #Use validators module



    Object Oriented Programming

    # a Tuple is like a list but inmutuble. And also is in parentesis.
    # If I  return using [] it returns a list.

    #classes allow you to invent your own data types in Python and give them a name.
    #You declare a class and then you declare a variable = that class
    #Then you add variable.xxx = xxxxx and so on.
    #When you create a class you create an object.

    #Another and better way of using classes and with instance methods using __init__
    #Now we are adding variables to objects (instance variables to objects).
    #A method is a function inside of a class.
    #Using raise error with message.
    #Printing directly the variable witch got the class but defaning __str__
    #To implement methods you have to defined a function with at least self as an argument.
    #properties --- @properties
    #Getter and Setter 
    #You can't repeat the name of the function as the variables. Thats why for convenction you have to put an underscore in front of the instance variable's name when setting.

    #@classmethod
    #Using class variables, without defining __init__ neither calling the class but using it directly.