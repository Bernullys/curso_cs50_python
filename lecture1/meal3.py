def main():
    # Prompt the user for a time (24 hrs format) as #:## or ##:##
    entry_24_format = input("What time is it? ")
    time_as_float = convert(entry_24_format)
    if time_as_float >= 7 and time_as_float <= 8:
        print("breakfast time")
    elif time_as_float >= 12 and time_as_float <= 13:
        print("lunch time")
    elif time_as_float >= 18 and time_as_float <= 19:
        print("dinner time")

def convert(time):
    #convert the input into a string in 24 hr format as a float
    hr, min = time.split(":")
    new_hr = float(hr)
    new_min = float(min)
    time_as_float = new_hr + round(new_min/60, 1)
    print(time_as_float)
    return time_as_float

if __name__ == "__main__":
    main()