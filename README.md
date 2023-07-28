# curso_cs50_python
I'm going to put here notes of every clase and exercice of this course

```py

    # if the name of a variable is in capitals it means is a constant.
    # even though you can change it is by design of python.

    print()
    print("\n")                             #Imprime una linea vacia
    print(end="")                           #Imprime y termina de una vez
    print(sep="")                           #esto imprime una separacion con el caracter que definamos - usable con dicts 
    print(var\n *3, sep="character")        #esto imprimira tres veces la variable enla misma linea separada por un caracter
    
    print("hello, "friend"")                #arroja error
    print("hello, \"friend\"")              #esto solucionaria -- el backslash siempre rompe el significado del caracter en este lenguaje
    print("hello, 'friend'")                #esto seria otra solucion pero menos usada

    print(f"str {variable}")               #str que queramos
    print(f"{number:,})                     #print a number with 1,000 format
    print(f"{float:.nf})                    #print a float with n decimals
    print(f"{float:,.nf})                   #print a convination of the above two

    input()
    int()
    float()
    round(number,n)                         #round to n decimals       
    pow(x,n)                                #returns the power of x to the n
    range()                                 #return  the range of the argumente
    range(a, b)                             #return the range between a and b

    def main():
    def function(arguments):
    return
    funtion(parameters)
    if__name__=="__main__":
        main()
    def function_name(other_function, argument):    #this is functional programming.
    def pure_function(x, y):                        #this is a pure function.
        temp = x + 2*y
        return temp / (2*x + y)
    some_list = []                                  #this is an impure function
    def impure(arg):                                #because it will change the state of some_list
        some_list.append(arg)

    # If a variable is declare outside of a function and you want to use it inside of a function you can use global:
    global var

Int Methods:

    abs()                                       # retorna el valor absoluto de un numero
    range(n)                                    # provides back n values

Lists Methods:

    list(range(a, b, c))                        #returns a list from a to b without including b and uses c to pass item by c times

    .len()                                       # returns the length of the variable or list or str or dict.
    .sorted()                                    #ordena en orden alfabetico
    .len()                                       # returns the length of the variable or list or str
    .append()                                   #is used with a for or while loop to make a list or in the right way to make a dict. The list has to be outside the loop.
    .clear()                                    #clears the list
    .copy()                                     #makes a copy of the list
    .count()                                    #returns the number of times the item is in the list
    .extend()                                   #adds the items of the list to the end of the list
    .index()                                    #returns the index of the item
    .insert(1, "X")                             #adds the item to the index. The first argument is the position index, the second is the item
    .pop()                                      #removes the item from the list
    .remove()                                   #removes the item from the list
    .sort()                                     #sorts the list
    .sort(reverse=True)                         #sorts the list reverse
    .sort(key=lambda x: x.lower())              #sorts the list by the item
    .reverse()                                  #reverses the list
    .max(a)                                      #return the maximum value of a list
    .min(a)                                      #returns the minimum value of a list
    x = [[0, 1, 2],
         [9, 8, 7]]                              #x[row][colum]

Dicts Methods:                                  #keys can not be itarable like list or dicts
                                                #to check for a key in a dict we can use in and not in

    .get(a,b)                                   #returns a value of a key a or if not in that dict returns b
    .value()                                    #returns the value of a key in a dict
    .update()                                   #to sum a dict into other.
    .pop(key_name)                              #to delete a key-value from a dict.
    del dict_name[key_name]                     #to delete a key-value from a dict.

Manipulating list of dict:

    To access a specific value in a dictionary, you can use indexing or the get() method.
    Example: my_list[0]['key'] or my_list[0].get('key').

    You can modify values in a dictionary by assigning a new value to a specific key.
    Example: my_list[0]['key'] = new_value.

    You can append a new dictionary to the list using the append() method.
    Example: my_list.append({'key': value}).

    You can remove a dictionary from the list using the remove() method or a list comprehension.
    Example: my_list.remove({'key': value}) or my_list = [item for item in my_list if item['key'] != value].

    You can use list comprehensions or the filter() function to filter dictionaries based on certain conditions.
    Example using list comprehension: filtered_list = [item for item in my_list if item['key'] == value].
    Example using filter() function: filtered_list = list(filter(lambda item: item['key'] == value, my_list)).


Strings Methods:

    str.strip()                             #remove whitespace from the str
    str.rstrip()
    str.title()                             #capitalize the first letter of each word
    str.lower()
    str.upper()
    str.casefold()
    str.capitalize()
    str.replace("lo_que_sea", "por_otra_cosa_que_sea")
    var1, var2 = varx.split(":") //de una variable con una entrada dividida por un caracter los separa desde donde se ponga el caracter
    str.startswith()
    str.endswith()
    str.isupper()                               #returns True or False if the str is upper
    str.islower()                               #returns True or False if the str is lower
    str.isdigt()                                #entrega True or False si es que el str contiene solo digitos no simbolos o puntuación.
    str.index()                                 #entrega el indice de la letra del string - la letra va dentro de los parentesis con comillas
    str.isalpha()
    str.isalnum()
    str.removeprefix()                          #remove the begginning of a string
    str.removesuffix()                          #remove the end of a string
    str.count()                                 #entrega el numero de veces que aparece la letra
    str.find()                                  #entrega el indice de la letra en la cadena
    str.rfind()                                 #entrega el indice de la letra en la cadena en orden inverso
    str.format()                                #to use with lists and strings (lookout documents). - Is use to print the index items of a list or str in {}
    str.join()                                  #to join the content of a list to a str
    str.split("")                               #returns a list from a str


Tuples:

    # Use tuples when your data cannot/should not change.
    # Tuples are immutable.
    # Thar means you can not reassign a value in a tuple like you can with list and dicts.

    tuples = ()                                #creates an empty tuple
    tuples = (1,2,3)                           #creates a tuple with 3 values
    tuples = "a", "b", "c"                     #creates a tuple with 3 values without parentheses
    # you can call a tuple using index like with lists
    variable = (1, 2, 3)
    a, b, c = variable                          #this will unpack a tuple
    a, b, c = [1, 2, 3]
    a, b, c = c, a, b                           # this will change the asignation
    a, b, *c, d = [1, 2, 3, 4, 5, 6, 7]         #this will asigne the extras to c

Sets:

    # Use a set if you need uniqueness for the elements.
    # Sets can not be indexed.
    # Its elements can be check with in and not in.
    # Sets can not contain duplicate elements.
    # len() can be use in sets.

    n_set = { 1, 2, 3, 4, 5}
    printing a set will remove all the similar elements
    n_set.add(7)
    n_set.remove(3)
    n_set.isdisjoint(n_set)                     #returns True or False if the sets are disjoint
    # operations with sets:
    set_one | set_two                           # will put together the elements that has no repet
    set_one & set_two                           # will put together the elements that has all the repet
    set_one - set_two                           # eliminara de set_one los que tenga iguales set_two
    set_one ^ set_two                           # crea un set con los elementos que no se repiten

Shortcuts:

    windows + .                                 #window of emojis 👌
    ctrl + d                                    #send a EOFError
    ctrl + c                                    #stop runing the code

Math Operators:

    + - * / % //

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




    NOTA: me di cuenta de que si en una funcion se regresa solo True o solo False siempre se regresara ese booleano asi la condicion no se cumpla.
    Por otro lado tengo que tener presente de que si se quiere probar varias condiciones, se pueden probar las condiciones falsas menos una.


Lists:

    # When to use a list:
    # if you have a collection of data that does not need random access.
    # When you need a simple, iterable collection that is modified frequently.


    var_lists = [0, 1, 2, ..., n]               # list are the equivalent of arrays in javascript

    if variable in var_lists:
        check if the variable is in the list

    if variable not in var_lists:
        check if the variable is not in the list

Dicts:

    # Whe to use a dictionary:
    # When you need a logical association between a key:value pair.
    # When you need fast lookup for your data, based on a custom key.
    # When your data is being constantly modified.
    # When you need to iterate over the data.
    # Dictionaries are mutable.


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

    # at grocery.py in lecture3 is how to create a dict and how to print it

    dict_name[var_key] = var_valeu              # this is how you can add key, value to a dict.

    sum_of_dicts = {**dict1, **dict2}           #this is to sum up two dicts.
    dict1.update(dict2)                         #this is to sum up two dicts.

Slices:

    str[n:]
    str[0:n]
    list[0:n]


Exceptions:

    #They occur when something goes wrong, due to incorrect code or input.
    #Defferent exceptions are raised for differents reasons like:
        ImportError #an import fails.
        IndexError #a list is indexed with an out-of-range number.
        NameError #an unknown variable is used.
        SyntaxError #the code can't be parsed properly.
        TypeError #a function is called on a value of an inappropriate type.
        ValueError #a function es called on a value of the correct type, but with an inappropriate value.
        ZeroDivisionError
        OSError

    #A try statement can have a multiple different except blocks to handle different exceptions.
    #Also multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
    #An except statement without any exceptions specified will cath all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes. Is useful when dealing with user input.

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
    p = inflect.engine()                                #this two lines come together

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

    import validators                                   #to validate specifics inputs

    mypy                                                #helps noticing the type of a variable executing mypy file_name.py 

    import argparse                                     # To manage argumentes from the user like sys but diferent.

     import csv

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
    #Always watch the cs50 classes
    #Use validators module



    Object Oriented Programming


    #First notes:

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

    #Exist another decorators.

    #inheritance is whereby you can define multiple classes that somehow relate to one another.
    #super().__init__() is a super class that can inheritance.

    #operator overloading

    # Notes from Sololearn:
        #Classes are created using the keyword class and an indented block, which contains class methods (methods are functions inside a class).
        #When creating a class you are making an instance (object).
        #The __init__ method is the most important method in a class. This is called when an instance of the class is created. The __init__ method is called the class constructor.
        #All methods must have self as their first parameter, although it isn't explicity passed, Python adds the self argument to the list for you; you don't need to include it when you call the methods. Whiting a method definition, self refers to the instance calling the method.

        #Inheritance
            #To inherit a class from another class, put the superclass name in parentheses after the class name.
            #A class that inherit from another class is called a subclass.
            #A class that is inherit from is called a superclass.
            #If the super and sub classes had the same method, the subclass will be the one.
            super() #is a function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.

        #Magic Methods
            #Are special methods which hable double underscores at the beginning and end of their names. Also known as dunders.
            #They are used to create functionality that can't be represent as a normal method.
            #Magic methods for common operators: (There are equivalent r methods for all magic methods)

                __add__ (+)
                __sub__ (-)
                __truediv__ (/)
                __floordiv__ (//)
                __mod__ (%)
                __pow__ (**)
                __and__ (&)
                __xor__ (^)
                __or__ (|)

                #the expression x + y is translated to x.__add__(y).
                #However, if x hasn't implement __add__, and x and y are two different types, then y.__radd__(x) is called.

            #Magic methods for comparisons:
                __lt__ (<)
                __le__ (<==)
                __eq__ (==)
                __ne__ (!=)
                __gt__ (>)
                __ge__ (>=)

                #if __ne__ is not implemented, it returns the opposite of __eq__

            #Magic methods for making classes act like containers:
                __len__ #for len()
                __getitem__ #for indexing
                __setitem__ #for assigning to indexed values
                __delitem__ #for deleting indexed values
                __iter__ #for iteration over objects (e.g., in for loops)
                __contains__ #for in

        # Data Hiding: (encapsulation)
            #Weakly private methods and attributes have a single underscore at the beginning. This signals that they are private.
            #Strongly private methos and attibutes have a double underscore at the beginning (mangled). The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

        # Class Methods:
            #Class methods are called by a class, which is passed to the cls parameter of the method.
            #A common use of these are factory methods, which instatiate an instance of a class, using different parameters than those usually passed to the class constructor.
            #Class methods are marked with a classmethod decorator.

        #Static Methods:
            #Are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
            #Static methods are marked with the staticmethod decorator.
            #Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.

        #Properties:
            #Provide a way of customizing access to instance attributes. They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. One common use of a property is to make an attribute read-only.
            #Properties can also be set by defining setter/getter functions:
                #The setter function sets the corresponding property's value.
                #The getter gets the value.
                #To define a setter or a getter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.






    class Class_name:
        def __init__(self, param1, param2):                                             # .param1 and .param2 are attributes of this class
            self._param1 = param1
            self.param2 = param2
        def __str__(self):
            return f"{self.param1} + {self.param2} = {self.param1 + self.param2}"       # or whatever you want to print when printing the class

        @property                                                       # this is to block param1 attribute and can't be modified (getter)
        def param1(self):
            return self._param1
        
        @param1.setter                                                  # this is to set the value of that property only if validate that condition (setter)
        def param1(self, param1):                                       
            if param1 < 0:                                              # whatever condition
                raise ValueError("param1 can't be negative")
            self._param1 = param1


    object_name = Class_name(xx, yy)
    print(object_name)                                                    #it can be printed because the str method is declared


    # Class method:

    @classmethod
    def funtion_name(cls, param1):
        return cls.param1
    
    Class_name.funtion_name()


    # Inheritance:

    class Parent:
        def __init__(self, param1,param2):
            self.param1 = param1
    class Son(Parent):
        def __init__(self,param3):
            super().__init__(param1, param2)
            self.param3 = param3

    son = Son(xx, yy, zz)


    # Explicación de atributos y propiedades por chatgpt:

    En las clases, tanto los atributos como las propiedades son elementos que pueden almacenar información y comportamiento relacionado. Sin embargo, hay una distinción conceptual entre ellos.

    Los atributos son variables que se declaran dentro de una clase y almacenan datos específicos para cada instancia de la clase. Estos atributos definen el estado o las características de un objeto. Los atributos pueden ser variables de instancia (asociadas a una instancia específica de la clase) o variables de clase (compartidas por todas las instancias de la clase). Se definen utilizando asignaciones dentro de la clase.

    Aquí hay un ejemplo que muestra atributos en una clase Person:

    class Person:
        def __init__(self, name, age):
            self.name = name  # Atributo de instancia
            self.age = age  # Atributo de instancia

        species = "Human"  # Atributo de clase

    person1 = Person("Alice", 25)
    print(person1.name)  # Acceso al atributo de instancia
    print(person1.age)  # Acceso al atributo de instancia
    print(Person.species)  # Acceso al atributo de clase

    En contraste, las propiedades proporcionan una forma de acceder y modificar valores asociados a un objeto, pero de manera controlada y con una lógica adicional. Se definen utilizando decoradores o métodos especiales llamados getter y setter. Las propiedades permiten realizar operaciones personalizadas durante el acceso o la modificación de un valor.

    Aquí hay un ejemplo que muestra el uso de propiedades en una clase Circle para el radio:

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            return self._radius

        @radius.setter
        def radius(self, value):
            if value > 0:
                self._radius = value
            else:
                raise ValueError("Radius must be a positive value.")

    circle = Circle(5)
    print(circle.radius)  # Acceso a la propiedad

    circle.radius = 10  # Modificación de la propiedad
    print(circle.radius)  # Acceso a la propiedad después de la modificación


    En este ejemplo, la propiedad radius permite acceder y modificar el atributo _radius de la clase Circle, pero al mismo tiempo realiza una validación para asegurarse de que el valor del radio sea mayor que cero.

    En resumen, los atributos son variables que almacenan datos específicos para cada instancia de una clase, mientras que las propiedades proporcionan métodos personalizados para acceder y modificar valores asociados a un objeto. Ambos conceptos son importantes en la programación orientada a objetos y se utilizan para modelar el estado y el comportamiento de los objetos en Python.



    List comprehensions:

    # Examples:
    a_list = [i**2 for i in range(5)]
    b_list = [i for i in range(5) if i % 2 == 0]
    c_list = [i for i in range(5) if i % 2 == 0 if i > 2]
    d_list = [i for i in range(5) if i % 2 == 0 if i > 2 if i < 3]
    e_list = [arg.upper() for arg in words]



    Lambdas:
    #known as anonymous.
    #Are used when passing a simple function as an argument to another function.
    #syntax: lambda - argument - : - expression to evaluate and return - parameter.

    my_function(lambda x: 2**x, 5) # this is defining a function.

   a = (lambda x: 2**x) (5) # this is using it right away.

    #lambdas can only do things that require  single expression



    Map:
    #Operate on list or similar objects called iterables.
    #Takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.
    # Examples:
    result = list(map(lambda x: x+5, nums)) #where nums is a list. It will return each element of the list + 5.
    
    

    Filter:
    #Filters an iterable by leaving only the items that match a condition (also called a predicate).
    # Examples:
    result = list(filter(lambda x: x > 5, nums)) #where nums is a list. It will return only the elements of the list that are greater than 5.
    


    Generators:
    #Generators are lazy (they do not evaluate the expressions until they are needed).
    #Are a type of iterable like list or tuples, but they don't allow indexing, but they can be iterated through for loops.
    #Uses the key word yield
    #are better than lists because don't have memory restrictions.
    #yield iterated and can be stored in a list using the function list.
    # Example: the function behaves like an iterator.
    def numbers(x):
        for i in range(x):
            if i % 2 == 0:
                yield i         # yield replace return in a function
    print(list(numbers(10)))



    Decorators:

    #Decorators modify functions using other functions.
    #This is ideal when you need to extend the functionality of functions that you don't want to modify.
    #Example:
    def decor(func):
        def wrap():
            print("---------")
            func()
            print("---------")
        return wrap

    @decor
    def print_text():
        print("Hello world!")
    
    print_text()



    Recursion:

    #Use in functional programming.
    #functions calling themselves.
    #recursion functions needs a base case. A case that dosen't involve any further calls to that function.
    #recursion can also be indirect. One function can call another function and another and make a circule.
    #I don't understand - Check the exercices in practice.



    *args

    #Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
    #The arguments are then accesible as the tuple args in the body of the function.

    **kwargs

    #key word arguments allows you to handle named arguments that you have not defined in advance.
    #The keyword arguments return a dictionary in which the keys are the arguments names, and the values are the argument values.

