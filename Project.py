'''
SCC5830 - Image Processing
Final Project
2019 - 1st semester

Image restoration: Sinusoidal noise removal
 
'''


import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftn, ifftn, fftshift
import imageio


def get_img():
    filename = str(input()).rstrip()
    img = imageio.imread(filename)
    return img

img = get_img()
plt.imshow(img, cmap = "gray")

def filter(img):
    fimg = fftn(img)
    return fimg


fimg = fftn(img)
print(img.shape)
print(fimg.shape)
print(np.min(fimg))
print(np.max(fimg))

plt.figure()
plt.imshow(np.log(1+np.abs(fftshift(fimg))), cmap = "gray")

#image shows 