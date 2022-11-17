def main():

    greeting = greetings(input("Greeting: "))


def greetings(a):

    greeting = a.strip().casefold()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
    
    return greeting

main()
