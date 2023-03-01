def main():

    fuel_gauge = input("Fraction: ")
    tank = get_a_correct_input(fuel_gauge)
    if tank <= 1:
        tank = "E"
    elif tank >= 99:
        tank = "F"
    else: tank = tank

    print(tank,"%")
     

def get_a_correct_input(fuel_gauge):
    while True:
        try:
            x, y = fuel_gauge.split("/")
            x = int(x)
            y = int(y)
            tank = int((x/y)*100)
        except ValueError:
            print("Input should have this format: intenger/intenger")
        else:
            break
        return tank

main()