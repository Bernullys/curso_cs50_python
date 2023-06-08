def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if valid_lengh(s) and first_two(s) and third_one(s) and last_part(s):
        return True
    else:
        return False

def valid_lengh(v_l):

    if len(v_l) < 2 or len(v_l) > 6:
        return False
    else:
        return True

def first_two(f_t):

    if len(f_t) >= 2:
        if f_t[0:2].isalpha():
            return True
        else:
            return False

def third_one(t_one):

    if len(t_one) >= 3:
        if t_one[2] == "0":
            return False
    return True

def last_part(l_part):
    if len(l_part) >= 3:
        for c in l_part:
            if c.isdigit():
                numb = l_part.index(c)
                if l_part[numb:].isdigit():
                    return True
                else:
                    return False
    return True

if __name__=="__main__":
    main()