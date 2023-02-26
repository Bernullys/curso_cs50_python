def main():
    now = input("WHat time is it? ")
    food_time = convert(now)
    
    if 7 <= food_time <= 8:
        print("Is breakfast time")
    elif 12 <= food_time <= 13:
        print("Is lunch time")
    elif 18 <= food_time <= 19:
        print("Is dinner time")

def convert(time):

    # time = time.replace(":", "")
    hr, sec = time.split(":")
    hr = float(hr)
    sec = float(sec)
    food_t = hr + (sec*99/60)/100
    return food_t

main()