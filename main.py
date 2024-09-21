from PIL import Image, ImageFilter

img_cat =  Image.open('images/cat.jpg')
filtered_img = img_cat.filter(ImageFilter.BLUR)



# print("Format of Image ",img_cat.format)
# print("Size of Image ",img_cat.size)
# print("Coloring Mode ", img_cat.mode)
#
# filtered_img.save("blur.png","png")

'''Converting Image'''
# converted_img = img_cat.convert("L")
# converted_img.save("converted.png","png")

# img_cat.show()



# with Image.open("lazz_animal.jpg") as lazzy_an:
#     resized_lazzy_an = lazzy_an.resize((250,250))
#     resized_lazzy_an.save("resized.png","png")
#     box = (100,100,500,500)
#     cropped_lazzy_an = lazzy_an.crop(box)
#     cropped_lazzy_an.save("cropped.png","png")


with Image.open('dodge_challenger.jpg') as dodge_pic:
    print(dodge_pic.size)
    resized_dodge_pic = dodge_pic.resize((250, 310))
    resized_dodge_pic.save('dodge_challenger_resized.jpg')

    dodge_pic.thumbnail((250, 310))
    dodge_pic.save('dodge_challenger_thumbnail.jpg')
    print(dodge_pic.size)
