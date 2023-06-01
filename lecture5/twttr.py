def main():
    twit = input("Input: ")
    twt = shorten(twit)
    print(f"Output: {twt}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    twt = ""
    for letter in word:
        if letter in vowels:
            twt = twt
        else:
            twt += letter
    return twt

if __name__ == "__main__":
    main()