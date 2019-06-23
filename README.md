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

