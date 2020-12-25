from PIL import Image, ImageOps

img = Image.open('./img/img00.jpg')
w, h = img.size

pixels = img.convert('RGBA')
data = img.getdata()
array_pixel = []

gray_img = ImageOps.grayscale(img)
#gray_img.show()
gray_data = gray_img.getdata()



ascii_file = open('./ascii-result.txt', 'w')

count=0
for x in range(h):
    ascii_file.write('\n')
    for y in range(w):
        if(0 <= gray_data[count] < 25):ascii_file.write('@')
        elif(25 <= gray_data[count] < 50):ascii_file.write('%')
        elif(50 <= gray_data[count] < 75):ascii_file.write('#')
        elif(75 <= gray_data[count] < 100):ascii_file.write('*')
        elif(100 <= gray_data[count] < 125):ascii_file.write('+')
        elif(125 <= gray_data[count] < 150):ascii_file.write('=')
        elif(150 <= gray_data[count] < 175):ascii_file.write('-')
        elif(175 <= gray_data[count] < 200):ascii_file.write(':')
        elif(200 <= gray_data[count] < 225):ascii_file.write('.')
        elif(225 <= gray_data[count] <= 255):ascii_file.write(' ')
        count+=1
ascii_file.close()
