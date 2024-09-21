from PIL import Image
import sys
import os


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# check if new/ exists, if not create
for filename in os.listdir(image_folder):
    # Loop through first folder
    # convert images to png
    # save to the new folder
    img = Image.open(f"{image_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f"{output_folder}/{clean_name}.png", "png")

