def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.casefold()
    if greeting.startswith("hello"):
        amount_to_people = "0"
    elif greeting.startswith("h"):
        amount_to_people = "20"
    else:
        amount_to_people = "100"

    return amount_to_people


if __name__ == "__main__":
    main()