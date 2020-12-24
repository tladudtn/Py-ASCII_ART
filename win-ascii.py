import os
from PIL import Image, ImageOps

img = Image.open('./img/img01.jpg')
w, h = img.size

pixels = img.convert('RGBA')
data = img.getdata()
array_pixel = []

gray_img = ImageOps.grayscale(img)
#gray_img.show()
gray_data = gray_img.getdata()


os.system('@echo off')
os.system('mode con cols={0} lines={1}'.format(w,h))


count = 0
for x in range(h):
    for y in range(w):
        if(0 <= gray_data[count] < 25):print('@',end='')
        elif(25 <= gray_data[count] < 50):print('#',end='')
        elif(50 <= gray_data[count] < 75):print('$',end='')
        elif(75 <= gray_data[count] < 100):print('&',end='')
        elif(100 <= gray_data[count] < 125):print('%',end='')
        elif(125 <= gray_data[count] < 150):print('?',end='')
        elif(150 <= gray_data[count] < 175):print('!',end='')
        elif(175 <= gray_data[count] < 250):print(':',end='')
        elif(250 <= gray_data[count] <= 255):print(' ',end='')
        count+=1

