import sys
from PIL import Image, ImageOps
import os

inputs_spliter = os.path.splitext(sys.argv[1])
outputs_spliter = os.path.splitext(sys.argv[2])

if inputs_spliter[1] != outputs_spliter[1]:
    sys.exit("Input and output have different extensions")

valid_extensions = [".jpg", ".jpeg", ".png"]
if inputs_spliter[1] not in valid_extensions:
    sys.exit("Input with invalid extension")

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("The specified input does not exist")


my_image = Image.open(sys.argv[1])
cs50shirt = Image.open("shirt.png")

size = cs50shirt.size
my_sized_image = ImageOps.fit(my_image, size)

my_sized_image.paste(cs50shirt, cs50shirt)
my_sized_image.save(sys.argv[2])
