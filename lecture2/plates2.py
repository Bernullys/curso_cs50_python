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
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else: 
                break
        i += 1
    
    marks = [".", " ", ",", ";", "!", "¡"]
    for m in s:
        if m in marks:
            return False

    return True

main()