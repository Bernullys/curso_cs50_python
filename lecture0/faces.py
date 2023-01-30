# this is the first program using functions
# as I described in my notebook: I use a variable as an argument and another as an helper.
# the argument is inside the function and the helper in the definition of the function, doing whatever the function needs to do with de argument. Then I return the helper so its value can be used.
# What the function convert do is to change a string that include :) or this :( into emoticons. And those emoticons were givent by the course.

def main():

    c = convert(a = input(""))

    print(c)

def convert(a):
    c = a.replace(":)", "🙂").replace(":(", "🙁")
    return c

main()