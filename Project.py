'''
SCC5830 - Image Processing Project
2019 - 1st semester

Image restoration: Periodic noise removal
Gabriel Gazetta - 10877911
 
'''

#read libraries
import numpy as np
from scipy.fftpack import fftn, ifftn, fftshift, ifft2
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import matplotlib.image as mpimg
import warnings
warnings.filterwarnings("ignore")

#function to read image
def get_img():
    filename = str(input("Image address: ")).rstrip()
    img = imageio.imread(filename)
    return img


#function to convert image from space domain to frequency domain
def spatialtofreq(img):
    ftimg = fftn(img) 
    ftimg = fftshift(ftimg)
    return ftimg

# definition of butterworh band-reject mask
def butterworth(euclideand, cutofffrequency, bandwidth, order):
    result = 1/(1+((euclideand*bandwidth)/((euclideand**2)-(cutofffrequency**2)))**(2.*order))
    return result

# definition of gaussian band-reject mask
def gaussian(euclideand, cutofffrequency, bandwidth):
    result = 1-np.exp(-((euclideand**2-cutofffrequency**2)/(euclideand*bandwidth))**2)
    return result

# function to calculate distance in notch filter
def in_circle(x,y,u,v,r):
    dist_from_center = np.sqrt(np.square(u-x) + np.square(v-y))
    return(dist_from_center <= r)

# ideal-notch filter
def notch(filter, array, r):
    for line in array:
        x = line[0]
        y = line[1]
        for u in range(x-r,x+r+1):
            for v in range(y-r,y+r+1):
                if in_circle(u,v,x,y,r):
                    try:
                        if u>=0 or v>=0:
                            filter[u,v] = 1
                        else:
                            pass
                    except:
                        pass
    return filter

#function that calls out the methods required and reads inputs.
def Filter(img, type):
    m,n = np.shape(img)
    imgout = np.zeros((m,n))
    cx = np.floor(m/2)+1
    cy = np.floor(n/2)+1
    if(type == "notch"):
                notches = np.array(eval(input("Insert array with coordinates ")))
                r = int(input("Insert notch radius "))
                imgout = notch(imgout, notches, r)
                imgout = 1 - imgout
    elif type == "butterworth" or "gaussian":
        bandwidth = int(input("Bandwidth: "))
        cutofffrequency = int(input("Cut-off Frequency: "))
        order = int(input("Order (filter sharpness): "))
        for x in range(m):
            for y in range(n):
                euclideand = np.sqrt((x-cx)**2+(y-cy)**2)
                if(type == "butterworth"):
                    imgout[x,y] = butterworth(euclideand, cutofffrequency, bandwidth, order)
                elif(type == "gaussian"):
                    imgout[x,y] = gaussian(euclideand, cutofffrequency, bandwidth)
    return imgout
    
#convert image from frequency domain back to spatial domain
def freqtospatial(fimg,):
    image = np.abs(ifft2(fimg))
    image = image.astype(np.uint8)
    return(image)


def main():
    img = get_img()
    ftimg = spatialtofreq(img)
    type = (input("Insert type of filter: "))     
    res_filter = Filter(img, type)
    resulting_img = freqtospatial(np.multiply(ftimg,res_filter))
    mpimg.imsave("result.png",resulting_img, cmap = "gray")
    print("Image saved in folder.")


if __name__ == '__main__':
    main()
