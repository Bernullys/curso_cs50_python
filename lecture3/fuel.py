def main():

    fraction = correct_fraction()
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
            print("F")
    else:
        print(int(fraction),"%")

def correct_fraction():
    while True:
        try:
            fuel_gauge = input("Fraction: ")
            x,y = fuel_gauge.split("/")
            x = int(x)
            y = int(y)
            answer = (x/y)*100
            if answer < 100:
                return answer
            else: print("It can't be greater than 100%")
        except (ValueError, TypeError):
            print("Incorrect Value")    
        except (ZeroDivisionError):
            print("You can't divide by 0")
    
main()