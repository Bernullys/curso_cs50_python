a1 = ["arp", "live", "strong"]
a2 = ["livaly", "alive", "harp", "sharp", "armstrong"]

a1_lenght = len(a1)

# a1i va a ser la cuenta de los elementos en la lista a1

a1i = 0
a2i = 0

print(a1[a1i])
print(a2[a2i])

for letters_in_a1_elements in a1[a1i]: #arp
    a1_a1i_lenght = len(a1[a1i]) #3
    first_letter_in_a1_elements = letters_in_a1_elements[0] #a
    for letters_in_a2_element in a2[a2i]: #lively
        if letters_in_a2_element == first_letter_in_a1_elements: # l == a      i == a 
            #first_coincidance = a2[a2i].index(letters_in_a2_elements)
            print("esta")
        else:
            print("No esta")
a1i += 1