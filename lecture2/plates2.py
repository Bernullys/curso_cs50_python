def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    if 2 > len(s) or 6 < len(s):
            return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    for char in s:
        if char.isdigit():
            index = s.index(char)
            if s[index:].isdigit() and char != 0:
                return True
            else:
                return False
    return True
    
    marks = [".", " ", ",", ";", "!", "¡"]
    for m in s:
        if m in marks:
            return False

    return True

main()