def main():
    twitter = input("")
    twttr = shorten(twitter)
    print(twttr)

def shorten(word):
    
    twttr = ""
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter in vowels:
            twttr = twttr
        else:
            twttr += letter
    #twttr = "".join([letter for letter in word if letter not in vowels])
    return twttr

if __name__ == "__main__":
    main()