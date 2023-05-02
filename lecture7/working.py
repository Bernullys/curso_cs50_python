import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    hours = re.search(r"^([0-9]|1[0-2]):?([0-5][0-9])? ([A-P]M) to ([0-9]|1[0-2]):?([0-5][0-9])? ([A-P]M)$",s)
    if hours:
        hours_in_parts = hours.groups()
        first_part = new_format(hours_in_parts[0],hours_in_parts[1],hours_in_parts[2])
        second_part = new_format(hours_in_parts[3],hours_in_parts[4],hours_in_parts[5])
        return f"{first_part} to {second_part}"
    else:
        raise ValueError

def new_format(hrs,mins,am_pm):
    if am_pm == "PM":
        if hrs == 12:
            new_hrs = 12
        else: 
            new_hrs = int(hrs) + 12
    else:
        if hrs == 12:
            new_hrs = 0
        else:
            new_hrs = int(hrs)

    if mins == None:
        new_mins = 0
        new_time_format = f"{new_hrs:02}:{new_mins:02}"
    else:
        new_time_format = f"{new_hrs:02}:{mins:02}"
  
    return new_time_format

if __name__ == "__main__":
    main()