import sys
from PIL import Image, ImageOps

#open an image with sys.argv
my_image = Image.open(sys.argv[1])
#print(my_image.format, my_image.size, my_image.mode)  --- this is just to know some parameters

#open the constant image
shirt = Image.open("shirt.png")

#define the desired size - using the same size for both images
size = (600, 600)
#or doing this:
#size = shirt.size
#change the size usin this functions
my_shirt_image = ImageOps.fit(my_image, size)

#overely the images
my_shirt_image.paste(shirt,(20, -80), shirt)

#save the new image with sys.argv
my_shirt_image.save(sys.argv[2])

