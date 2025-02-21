import pandas as pd
from matplotlib import pyplot as plt
from skimage.io import imread 
from skimage.transform import resize

image = imread(r"D:\kavy\web desining\logo.png")
croppedimage = image[0:100,0:200]

plt.imshow(image)
plt.show()

resized = resize(image,(300,200))
plt.imshow(resized)
plt.subplot(1, 2, 1)
plt.show()