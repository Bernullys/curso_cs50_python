import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    n = re.findall(r'.?\bu[m]\b *', s, re.IGNORECASE)
    return len(n)

if __name__ == "__main__":
    main()