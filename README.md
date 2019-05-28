# Skin Cancer Image Enhancement and Classification
##### SCC5830

#### Gabriel Gazetta de Araujo.  nº USP 10877911

### Abstract:
This final project aims to remove sinusoidal patterns from images. To do so, it is necessary to convert these images to the frequency domain through Fourier Transform in order to visualize and cancel out these high-frequency regions with specific filters.

#### Application: 
Image Restoration - Pattern and noise removal

#### Inputs: 
corrupted images with patterns (sinusoidal noise).
For the input, I've researched and chosen the following images with sinusoidal patterns on them for further removal.
* [Moon Landing Image](https://imgur.com/gallery/MHcHVmX) - uploaded by Hugh Bothwell
* [Lena](http://user.engineering.uiowa.edu/~dip/examples/images/lena_corrupt.png) - University of Iowa

#### Outputs: 
Processed Images without patterns.

### Methodology
It can be said that noise is not easily removed in the space domain, which means that for this project, I intend to transform images to the frequency domain and plotting them. This plot is likely to permit observing high-frequency points in the image, with that, it is possible to create a filter that goes through the frequency domain and cancels out these high-frequency areas, removing patterns from the image. 

* Step 1: Finding images with sinusoidal noise.
* Step 2: Applying the Fourier transform in these images and observing their behavior in the frequency domain.
* Step 3: Creating a band filter to apply gaussian, Butterworth and ideal knotch filters.
* Step 4: Plotting the resulting images and comparing the methods.

