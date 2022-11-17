def main():

    c = convert(a = input(""))

    print(c)

def convert(a):
    c = a.replace(":)", "🙂").replace(":(", "🙁")
    return c

main()