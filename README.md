# curso_cs50_python
I'm going to put here every exercice of this course

Lecture0 Functions

    print()
    print(var\n 3, end="")                  # esto imprime la variable 3 veces en lineas separadas y luego termina de una vez
    input()
    int()
    float()
    round(number,n)
    pow(x,n)

    def function():
    funtion()

    print(f"str ${variable}")                   # str que queramos
    (float: .nf)                                # decimal : cantidad_de_decimales f
    abs()                                       # retorna el valor absoluto de un numero

Lectures Methods:

    str.strip()
    str.lower()
    str.casefold()
    str.replace("lo_que_sea", "por_otra_cosa_que_sea")
    var1, var2 = varx.split(":") //de una variable con una entrada dividida por un caracter los separa desde donde se ponga el caracter
    str.startswith()
    str.endswith()
    str.isupper()
    str.islower()
    str.isdigt()                                #entrega True or False si el que el str contiene solo digitos no simbolos o puntuación.
    str.index()                                 #entrega el indice de un str
    str.isalpha()
    str.isalnum()


I have a question about when a function has to return more than one variable o print. How should be the return

09-02-2023

i != n # diferente de

while condition :

for condition: # for loops iterates through a list of items

range(n) # provides back n values

######## Pequeña funcion para comprobar una entrada ########
while True:
    n = int(input("What's n? ))
    if n > 0:
        break
    return n
#############################################################

var_lists = [0, 1, 2, ..., n]           # list are the equivalent of arrays in javascript

len                                     # len es el largo de la lista

dict or dictionaries is a data structure that allows you to associete keys with values.

var_dict = {                            # la parte de varn son las keys y la parte de las Varn.n son los valores de las keys - Un valor puede ser None
    var1: Var1.1, varX: VarX.1, ...
    var2: Var2.2, varY: VarY.1, ...
    ...
    varn: Varn.n, varN: VarN.1, ...
}

for var_dict_1 in var_dict:
    print(var_dict_1, var_dict[var_dict_1], sep=", ")       # Esto imprimiria las keys con sus valores deparados por coma y espacio

########## EXCEPTIONS #########################################

while True:
    try:
        code
        code
    except (error_type_1, ..., error_typy_n)
        code
        or
        try:
            code
            ...
            break
            else:pass   ### this will promp again for an input
    except (error_type_1, ..., error_typy_n)
        try:
            code
            else:pass
        except (error_type)
            pass
        

##### at grocery.py in lecture3 is how to create a dict and how to print it.

