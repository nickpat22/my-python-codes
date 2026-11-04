from PIL import Image
import numpy as np

img = Image.open("digit_28x28.png")
img = img.convert("L") 
img = img.resize((28,28))

pixels = np.array(img)

print("Image Size : ",pixels.shape)

print("Pixel Values : ")
print(pixels)

# 0         pure black
# 255       pure White
# 50        Dark Greay
# 120       Medium Grey
# 200       Light Grey