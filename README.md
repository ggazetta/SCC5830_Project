# Periodic noise removal
##### SCC5830

#### Gabriel Gazetta de Araujo.  nº USP 10877911

### Abstract:
Images with patterned noises can be difficult to process or even to visualize. These patterns are high-frequency noises that scatter throughout the images. With that said, this final project aims to design a code capable of removing sinusoidal patterns from images. In order to remove those patterns, it is necessary to convert the images to the frequency domain through Fourier Transform in order to visualize and cancel out those high-frequency regions with filters that cancels the specific high-frequency areas in the image, resulting in an image with no pattern and little to no blur.


#### Application: 
Image Restoration - Pattern and noise removal

#### Inputs: 
corrupted images with patterns (sinusoidal noise).
For the input, I've researched and chosen the following image with sinusoidal patterns on it for further removal.
* [Lena](http://user.engineering.uiowa.edu/~dip/examples/images/lena_corrupt.png) - University of Iowa

#### Outputs: 
Processed Images without patterns.

### Methodology

* Step 1: Finding images with sinusoidal noise.
* Step 2: Applying the Fourier transform in these images and observing their behavior in the frequency domain.
* Step 3: Creating a band-reject filter to apply gaussian, Butterworth filters.
* Step 4: Creating a notch filter to cancel out specific points on the image.
* Step 5: Plotting the resulting images and comparing the methods.


### Introduction

Periodic noises causes a range of problems in image visualization and even processing. In order to remove those noises from images, a variety of techniques can be adopted. Although filters can be used on the space domain, since these noises are periodic, it is generally a wiser decision to use the frequency domain.

### Methods and development

In this project, in order to remove noises the image was converted to the frequency domain throught a Fast Fourier Transform, and then plotted in the Fourier Spectra.

![Lena](/lena_corrupted.png)

**Figure 1** - Image with periodic noise selected to be treated.


![Fourier Spectra](/Notebook/fourierspectra.png)

**Figure 2** - Fourier Spectrum of the image above.

The Fourier Spectrum can be used to identify the regions on the image responsible for the noises. On the image above, eight points can be identified. In order to remove those points. Two different approaches were addopted in this project.
The first approach was to create a band-reject filter that creates a band on the frequency domain, and "rejects" the information inside that band. Two filters were adopted: butterworth and gaussian, the preferable is the butterworth, since it is possible to control the "sharpness" of the filter, by altering its order.

![Band-reject](/Notebook/band.png)

**Figure 3** - Butterworth Band-reject filter.

The second approach was to create a notch filter, which consists on selecting specific regions to "reject", or carve out. The results are images sharper and with more information than with images treated with band-reject filters, since they don't remove any info more than necessary.

![Notch](/Notebook/notches.png)

**Figure 4** - Ideal Notch filter.


### Results:

The following images were resulted from the filters:

Band-reject             |  Notch
:-------------------------:|:-------------------------:
![](/Results/result_band_butterworth.png)  |  ![](/Results/resulting_img_notch.png)

**Figure 4** - Comparison

### Conclusion
Although the images look similar, it can be noticed that the image on the right looks sharper and more detailed than the left one. That is due to the fact that a notch filter carves out as little as possible of the image, resulting in little to no loss in image information. Regarding that, it can be concluded that even though notch filters can take longer to point out the pixels, the result is better than a band-reject filter. In fact, notch filters can be the only option when treating very noisy images, in those cases, a band-reject filter would require a large width, causing the resulting image to lose too much information in a way that the result won't be satisfactory; because of that, in those cases, notch filters can be the only reasonable option.


### References:
* [CUFF, Paul. Frequency Domain and Fourier Transforms. Princeton University](https://www.princeton.edu/~cuff/ele201/kulkarni_text/frequency.pdf)
* [CATTIN, Philippe.Image Restoration. 2016.](https://miac.unibas.ch/SIP/pdf/SIP-06-Restoration.pdf)
* [LILIENTHAL, Achim. Noise Reduction. Lecture Notes. 2011.](http://130.243.105.49/Research/MRO/courses/dip/2011/lectures/DIP_2011_L09.pdf)
* [GeoSpatial. Band-Reject Filter](https://www.harrisgeospatial.com/docs/BANDREJECT_FILTER.html)

