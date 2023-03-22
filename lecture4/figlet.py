# to use pyfiglet#
from pyfiglet import Figlet
figlet = Figlet()

# to get a list of fonts #
figlet.getFonts()

# to set a font # Where the name of the fonts are in a link  and has to be in ""#
#### figlet.setFont(font="banner") #### donde banner es un tipo de letra#

import random 
import sys

if len(sys.argv) == 1:
    text_in = input("Input: ")
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=str(random_font))
    print(figlet.renderText(text_in)) 

elif len(sys.argv) == 3 and sys.argv[1] == "--font" or sys.argv[1] == "-f":
    if sys.argv[2] in figlet.getFonts():
        text_in = input("Input: ")
        figlet.setFont(font=str(sys.argv[2]))
        print(figlet.renderText(text_in))
    else: sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
