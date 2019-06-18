'''
scc5830 - Image Processing
Final Project
2019 - 1st semester

Image restoration: Sinusoidal noise removal
 
'''
import numpy as np
from scipy.fftpack import fftn, ifftn, fftshift, ifft2
import matplotlib.pyplot as plt
import imageio
from PIL import Image


def get_img():
    filename = str(input()).rstrip()
    img = imageio.imread(filename)
    return img


img = get_img()
plt.imshow(img, cmap = "gray")


def spatialtofreq(img):
    m, n = img.shape
    diff = abs(m-n)
    new_m, new_n = m, n
    if(m > n):
        new_n = n+diff
    else:
        new_m = m+diff  
    nimg = np.zeros((new_m,new_n))
    nimg[:m,:n] = img
    ftimg = fftn(nimg) 
    ftimg = fftshift(ftimg)
    #plt.imshow(np.real(nimg), cmap = "gray")
    return ftimg

def butterWorthFilter(euclideand, cutofffrequency, bandwidth, order):
        result = 1/(1+((euclideand*bandwidth)/((euclideand**2)-(cutofffrequency**2)))**(2.*order))
    return result


def gaussianFilter(euclideand, cutofffrequency, bandwidth):
        result = 1-np.exp(-((euclideand**2-cutofffrequency**2)/(euclideand*bandwidth))**2)
    return result

def createBandFilter(m, n, type, cutofffrequency, bandwidth, order):
    img = np.zeros((m,n))
    cx = np.floor(m/2)+1
    cy = np.floor(n/2)+1
    for x in range(m):
        for y in range(n):
            euclideand = np.sqrt((x-cx)**2+(y-cy)**2)
            if(type == "notch"):
                img[x,y] = #quero por o notch aqui
            elif(type == "butterworth"):
                img[x,y] = butterWorthFilter(euclideand, cutofffrequency, bandwidth, order)
            elif(type == "gaussian"):
                img[x,y] = gaussianFilter(euclideand, cutofffrequency, bandwidth)
    return img

rejectBandFilter = createBandFilter(m, n, "gaussian", cutofffrequency, bandwidth, 2)
plt.imshow(rejectBandFilter, cmap = "gray")


def freqtospatial(fimg, img):
    m, n = img.shape
    image = np.abs(ifft2(fimg))
    image = image.astype(np.uint8)
    crop_img = image[0:m, 0:n]
    return(crop_img)

filteredImageRejectBandIdeal =freqtospatial(np.multiply(ftimg,rejectBandFilter),img)
plt.imshow(filteredImageRejectBandIdeal, cmap = "gray"



def in_circle(x,y,u,v,r):
    dist_from_center = np.sqrt(np.square(u-x) + np.square(v-y))
    return(dist_from_center <= r)

def insert_point_on_filter(filter, x, y, r):
    for u in range(x-r,x+r+1):
        for v in range(y-r,y+r+1):
            if(in_circle(u,v,x,y,r)):
                filter[u,v] = 0    
    return filter


filter = np.ones((100,100), dtype=np.uint8)

filter = insert_point_on_filter(filter,25,25,8)


plt.figure(); plt.imshow(filter); plt.title("result of filter")

