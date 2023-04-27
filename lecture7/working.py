import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    hours = re.search(r"^([0-9])|(1[0-2]):?([0-5])([0-9])? (AM)?(PM)? to ([0-9])|(1[0-2]):?([0-5])([0-9])? (AM)?(PM)?$",s)
    if hours:
        hours = hours.groups()
        if hours.group(1):
        #     hrs1 = int(hours.group(1))
        # else: hrs1 = int(hours.group(2))
        # if hours.group(3):
        #     min_1 = int(hours.group(3) + hours.group(4))
        # else: min_1 = int("0" + hours.group(4))
            print(hours.group(1))


        # if hours.group(3):
        #     hrs = int(hours.group(1))
        #     min = int(hours.group(2))
        #     if hrs > 9 and min > 9:
        #         print(hrs,":",min, sep="")
        #     elif hrs > 9 and min < 9:
        #         print(hrs,":","0",min, sep="")
        #     elif hrs < 9 and min > 9:
        #         print("0",hrs,":",min, sep="")
        #     elif hrs < 9 and min > 9:
        #         print("0",hrs,":","0",min, sep="")

if __name__ == "__main__":
    main()