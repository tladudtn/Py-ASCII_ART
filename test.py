from PIL import Image


img = Image.open('./img01.jpg')
w, h = img.size

pixels = img.convert('RGBA')

data = img.getdata()

array_pixel = []


# count로 (w,h) 픽셀 RGB값 출력 
count=0
for x in range(w) :
    for y in range(h):
        print("{0}, {1} : {2}".format(x,y,data[count]))
        count+=1




