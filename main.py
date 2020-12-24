from PIL import Image

# import img
img = Image.open('./img.jpg')

# get width & height 
w, h = img.size

# L O A D
pixels = img.load()

# pixel data
all_pixel = []

for x in range(w):
    for y in range(h):
        cpixel = pixels[x, y]
        all_pixel.append(cpixel)


# print img width height  
print(img.size)

print(cpixel)