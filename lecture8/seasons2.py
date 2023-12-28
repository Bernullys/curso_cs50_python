from datetime import date, datetime, timedelta
import sys
import inflect
p = inflect.engine()

def main():

    date_birth = right_format_input(input("Date of Birth: "))
    y, m, d = formating_date(date_birth)
    date_of_birth = date(y, m, d)
    delta_days_lived = date.today() - date_of_birth
    minutes_lived = round(delta_days_lived.total_seconds()/60)

    singing_minutes_lived = p.number_to_words(minutes_lived, andword="")
    singing_minutes_lived = singing_minutes_lived.capitalize()
    print(f"{singing_minutes_lived} minutes")


def formating_date(d_birth):
    year, month, day = d_birth.split("-")
    year_num = int(year)
    month_num = int(month)
    day_num = int(day)
    return year_num, month_num, day_num


def right_format_input(i_d_b):
    try:
        if datetime.strptime(i_d_b, "%Y-%m-%d"):
            return i_d_b 
    except ValueError:
        sys.exit("Invalid date format")



if __name__ == "__main__":
    main()