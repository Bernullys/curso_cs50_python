def main():

    hr = convert(input("What time is it? "))

    if 7 <= hr <= 8:
        print("breakfast time")
    elif 12 <= hr <= 13:
        print("lunch time")
    elif 18 <= hr <= 19:
        print("dinner time")

def convert(time):

    min, seg = time.split(":")
    min = float(min)
    seg = float(seg)

    hr = float(min+(seg*99/60)/100)
    hr=round(hr, 1)
    print(hr)
    return hr

main()