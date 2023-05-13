from datetime import datetime, date
import sys
import inflect
p = inflect.engine()

def main():
     
    date_birth = validate_date(input("Date of Birth: "))
    year, month, day = split_date_format(date_birth)
    day_of_birth = date(year, month, day)
    today = date.today()
    delta = today - day_of_birth
    minutes = delta.days * 24 * 60
    minutes_in_words = p.number_to_words(minutes, andword="")
    print(f"{minutes_in_words.capitalize()} minutes")

def validate_date(d):
    try:
        format = datetime.strptime(d, "%Y-%m-%d")
        return d
    except: 
        return "Invalid date"

def split_date_format(df):
    a,m,d = df.split("-")
    annos = int(a)
    months = int(m)
    days = int(d)
    return annos, months, days

if __name__=="__main__":
    main()