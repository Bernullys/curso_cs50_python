def main():

    sttng_twttr = input("Input: ")

    twitter_set = deleting_vowels(sttng_twttr)

    print(f"Output: {twitter_set}")


def deleting_vowels(sttng_twttr):

    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

    twitter_set = ""

    for letter in sttng_twttr:

        if letter in vowels:
            twitter_set += ""
        else:
            twitter_set += letter
    
    return twitter_set

main()