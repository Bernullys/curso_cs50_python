def main():
    greeting = input("Greeting: ")
    payment = value(greeting)
    print(payment)


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        amount = 0
    elif greeting.startswith("h"):
        amount = 20
    else:
        amount = 100
    return amount

if __name__ == "__main__":
    main()