from PIL import Image
import numpy as np

img = Image.open("color.png")

img = img.resize((28,28))

pixels = np.array(img)

print("Image Information : ")
print("Image Shape :",pixels.shape)
print("Hight of Image : ",pixels.shape[0],"Rows")
print("Hight of Image : ",pixels.shape[1],"Columns")
print("Channels : ",pixels.shape[2],"(R,G,B)")


total = pixels.shape[0] * pixels.shape[1] * pixels.shape[2]
print("Total Pixels : ",total)

print("Single Pixel Meaning : ")

r = pixels[10][10][0]
g = pixels[10][10][1]
b = pixels[10][10][2]

print("Pixel Details of 10,10 pixel is :")
print("Red :",r)
print("Green :",g)
print("Blue :",b)