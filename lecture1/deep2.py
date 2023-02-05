def main():

    q = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

    if the_right_answer(q):
        print("Yes")
    else: print("No")


def the_right_answer(q):

    a = ["42", "forty two", "forty-two"]

    for i in a:
        if q == i:
            return True

main()