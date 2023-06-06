from datetime import date


def main():

    date_birth = input("Date of Birth: ")
    y, m, d = formating_date(date_birth)
    date_of_birth = date(y, m, d)
    
    date.today()

    


def formating_date(d_birth):
    year, month, day = d_birth.split("-")
    year_num = int(year)
    month_num = int(month)
    day_num = int(day)
    return year_num, month_num, day_num







if __name__ == "__main__":
    main()