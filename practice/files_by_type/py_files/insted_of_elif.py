
def pick_a_week_day(number_day):
    week_days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    print(week_days.get(number_day, "It has to be a number from 1 to 7"))

pick_a_week_day(3)

# I can also call it directly:

week_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

mon = week_days.get(2, "It has to be a number from 1 to 7")
print(mon)