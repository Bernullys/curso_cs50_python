import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"^([1-9]|[1-9][0-2])(?::)?([0-5][0-9])? (AM|PM) to ([1-9]|[1-9][0-2])(?::)?([0-5][0-9])? (AM|PM)$", s)
    if matches:
        h1, m1, meridiem1, h2, m2, meridiem2 = matches.groups()
        if meridiem1 == "AM":
            first_part = AM(h1,m1)
        elif meridiem1 == "PM":
            first_part = PM(h1,m1)
        if meridiem2 == "AM":
            second_part = AM(h2,m2)
        elif meridiem2 == "PM":
            second_part = PM(h2,m2)
    else:
        raise ValueError
    
    return f"{first_part} to {second_part}"

def AM(h,m):
    if int(h) < 10 and h != "12":
        h = f"0{h}"
    elif h == "12":
        h = "00"
    else:
        h = h
    if m != None:
        m = m
    else:
        m = "00"
    return f"{h}:{m}"

def PM(hr,min):
    if int(hr) != 12:
        hr = 12 + int(hr)
    else:
        hr = hr
    if min != None:
        min = min
    else:
        min = "00"
    return f"{hr}:{min}"

if __name__ == "__main__":
    main()