import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^([1-9]|[1-9][0-2])(?::)?([0-5][0-9])? (AM|PM) to ([1-9]|[1-9][0-2])(?::)?([0-5][0-9])? (AM|PM)$", s)
    if matches:
        h1, m1, meridiem1, h2, m2, meridiem2 = matches.groups()
        return m1
    
    else:
        raise ValueError

# def analays(matches_group):
#     hr, min, meridiam, hr2, min2, meridiam2 = 

if __name__ == "__main__":
    main()