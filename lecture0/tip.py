# this program is my first one with more than one function.
# to execute right this one you have to promp the first input using this format: $intint.intint and the second as intint%

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent/100)
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars = float(d.replace("$", ""))
    return dollars


def percent_to_float(p):
    percent = float(p.replace("%", ""))
    return percent


main()