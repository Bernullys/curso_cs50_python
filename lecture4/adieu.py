import inflect
p = inflect.engine()

names_list = ["Adieu, adieu"] #antes lo tenia "Adieu, adieu, to" pero al aplicarle el modulo para mas de 3 me ponia una coma despues del to
while True:
    try:
        name_in = input("Name: ")
    except EOFError:
        print()
        break
    names_list.append(name_in)

names_list[1] = "to " + names_list[1] # esto hace que no le ponga coma despues del to

if len(names_list) == 2:
    adieu_frase = p.join(names_list, conj="")
    print(adieu_frase)
elif len(names_list) == 3:
    adieu_frase = p.join(names_list, final_sep="")
    print(adieu_frase)
else: 
    adieu_frase = p.join(names_list)
    print(adieu_frase)

