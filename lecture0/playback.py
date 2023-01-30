# this program is replacing every space for three dots like is counting every word.
# Now I'm going to implement a function to do it.

def main():

    fasty = input("")
    play_back = pb(fasty)
    print(play_back)

def pb(fasty):

    play_back = fasty.replace(" ", "...")
    return play_back

main()
