def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    puntuations = ["|", "!", "#", "?", "¡", "¿", ",", ".", ";"]
    for l in s:
        if l in puntuations:
            return False
    if len(s) < 2:
        return False
    elif len(s) > 6:
        return False
    elif s[0:2].isalpha() == False:
        return False
    for letter in s:
        if letter.isdigit():
            key_d = s.index(letter)
            if s[key_d:].isdigit() and letter != "0":
                return True
            else:
                return False 
    return True


if __name__== "__main__":
    main()