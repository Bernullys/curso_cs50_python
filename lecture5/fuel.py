def main():

    g_fraction = convert(input("Fraction: "))
    percentage_final = gauge(g_fraction)
    print(f"{percentage_final}")

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x_int = int(x)
        y_int = int(y)
    except ValueError:
        raise ValueError
    else:
        try:
            fraction_float = x_int/y_int
            if y_int < x_int:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            try:
                fraction_float = x_int/y_int
            except ZeroDivisionError:
                raise ZeroDivisionError
            else:
                per100 = round(fraction_float*100)
                print(per100)
                return per100

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()