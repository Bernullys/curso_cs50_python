def main():
    convertion = convert()
    gauge_percent = gauge(convertion)
    if gauge_percent <= 1:
        print("E")
    elif gauge_percent >= 99:
        print("F")
    else:
        print(f"{gauge_percent:.0f}%")

def convert():
    while True:
        try:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            x_int = int(x)
            y_int = int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            try:
                if x_int <= y_int:
                    return x_int/y_int
            except ZeroDivisionError:
                pass

def gauge(percentage):
    percent = round(percentage*100, 0)
    return percent

if __name__ == "__main__":
    main()