def main():

    g = input("Greeting: ").strip().casefold()
    promises_check(g)

def promises_check(g):

    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else: print("$100")

main()
