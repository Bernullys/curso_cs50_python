def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif len(s) >= 2:
        ese = ""
        for letter in s[0:2]:
            ese += letter
        if first_two(ese) == False:
            return False
        if thirth_one != True:
            return False
        else:
            return True
        
def first_two(ese):
    if ese.isalpha():
        return True
    else:
        return False

def thirth_one(ese):
    if ese[2] == "0":
        return False
    else: return True
            


main()