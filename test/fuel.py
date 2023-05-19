def main():
    fraction = input("Fraction: ")
    convertion = convert(fraction)
    gauge_percent = gauge(convertion)

    print(gauge_percent)

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x_int = int(x)
            y_int = int(y)
        except (ValueError):
            pass
        else:
            try:
                if x_int <= y_int:
                    return x_int/y_int
            except ZeroDivisionError:
                pass

def gauge(percentage):
    percent = round(percentage*100)
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return str(percent) + "%"

if __name__ == "__main__":
    main()