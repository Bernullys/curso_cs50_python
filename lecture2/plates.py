def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
# length(plate):
    if 2 > len(plate) or 6 < len(plate):
        return False

# first_two(plate):
    two_first = plate[0:2]
    uppers = ""
    for letters in two_first:
        if letters.isupper() == True:
            uppers += letters
        else: uppers = uppers
    uppers_len = len(uppers)
    if uppers_len != 2:
        return False
    
 #   thirth_one (plate):
    if len(plate) >= 3:
        if plate[2:3] == "0":
            return False
        
# from_two_onwards_uppers(plate):
    i =  0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else: 
                break
        i += 1
    
    return True

main()




