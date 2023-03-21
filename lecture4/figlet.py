# to use pyfiglet#
from pyfiglet import Figlet
figlet = Figlet()

# to get a list of fonts #
figlet.getFonts()

# to set a font # Where the name of the fonts are in a link  and has to be in ""#
figlet.setFont(font="banner")

import random
import sys

text = input("Input: ")

print(text, sys.argv[1])