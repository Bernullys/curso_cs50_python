months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month,day,year = date.split("/")
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)
        if len(year) == 4 and day_int <= 31 and month_int <= 12:
            print(f"{year_int}","-",f"{month_int:02}","-",f"{day_int:02}", sep="")
            break
        else:pass

    except ValueError:
        try:
            month,day,year = date.split(" ")
            if day.endswith(","):
                day_int = int(day.replace(",", ""))
                if month in months and len(year) == 4 and day_int <= 31:
                    month_number = months.index(month) + 1
                    print(year,"-",f"{month_number:02}","-",f"{day_int:02}",sep="")
                    break
                else: pass

        except ValueError:
            pass
