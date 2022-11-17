def main():

    a = question(input("What is the Great Question of Life, the Universe and Everything? ").casefold().strip())

def question(q):

    if q == "42" or q == "forty two" or q == "forty-two":
        print("Yes")
    else:
        print("No")

main()
