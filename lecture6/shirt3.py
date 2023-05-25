# the program expects two command-line arguments:
# the first one the name or path of a JPEG or PNG to read as input.
# the second one the name or path of a JPEG or PNG to write as output.
import sys
from PIL import Image, ImageOps
import os

#Checks:
if len(sys.argv) > 3:
    sys.exit(" Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit(" Too few command-line arguments")

valid_extensions = [".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"]
root_image_in, ext_image_in = os.path.splitext(sys.argv[1])
root_image_out, ext_image_out = os.path.splitext(sys.argv[2])
if ext_image_in not in valid_extensions or ext_image_out not in valid_extensions:
    sys.exit(" Invalid extensions. Only .jpg, .jpeg, .png, .JPG, .JPEG, .PNG are valid extensions.")
elif ext_image_in != ext_image_out:
    sys.exit(" Input image and output image should have the same extension")
else:
    try:
        image_in = Image.open(sys.argv[1])
    except:
        FileNotFoundError
        sys.exit(" Input image not found")

#open an image:
before_image = Image.open(sys.argv[1])
# resize and cropping the input to shirt.png
# but first know the size of shirt.png:
shirt = Image.open("shirt.png") 
shirt_size = shirt.size
resize_image = ImageOps.fit(before_image, shirt_size)
# the program should overlay shirt.png on the input.
resize_image.paste(shirt, shirt)
# save the result as output
resize_image.save(sys.argv[2])