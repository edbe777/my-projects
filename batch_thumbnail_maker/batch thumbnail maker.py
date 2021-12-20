import os, sys
from PIL import Image

original = "C:\\Users\\eddie\\Desktop\\Ironhack\\MY PROJECTS\\images\\"
destination = "thumbnail_images_destination"

if not os.path.exists(destination):
    os.makedirs('batch_thumbnail_maker_images')

dirs = os.listdir(original)
print("BATCH_THUMBNAIL_MAKER")
thumb_width = int(input("Please enter the desired Thumbnail width in pixels, and press enter: "))
thumb_height = int(input("Please enter the desired Thumbnail height in pixels, and press enter: "))

for file in dirs:
    original_image= original + file
    print(original_image, "---converted_to_thumbnail")
    img = Image.open(original_image)
    resize = img.resize((thumb_width, thumb_height), Image.ANTIALIAS)
    resize.save("batch_thumbnail_maker_images/resized" + file + ".jpg")
print("DONE!")