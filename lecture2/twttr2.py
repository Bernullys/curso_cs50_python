def main():

    text_post = input("Input: ").casefold()

    twttr_pst = vowels_cutter(text_post)

    print("Output: ",twttr_pst)


def vowels_cutter(text_post):

    vowels = ["a", "e", "i", "o", "u"]
    twttr = ""
    for letters in text_post:
        if letters in vowels:
            twttr += ""
        else: twttr += letters
    return twttr


main()