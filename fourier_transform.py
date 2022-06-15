"""
    In this script, I have implement fourier transform to an image
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

# generate a 2D sine wave image
x = np.arange(256)  # generate values from 0-255
y = np.sin(2* np.pi * x/20)  # calculate sin of x values

# devide by a smaller number above to increase the frequency
y+= max(y)  # offset sine wave by the max vallue to go out of negative range of sine

# generate a 256 X 256 image(2D array of the sine wave)
img = np.array([[y[j]* 127 for j in range(256)] for i in range(256)], dtype= np.uint8)

# plotting image 
plt.imshow(img)
plt.title("Sine wave")
plt.show()

img = cv2.imread("Images/img_3.jpg", 0)  # load image

# output is a 2D complex array, 1st channel real and 2nd channel imaginary
# for fft in OpenCV input image need to be converted into float32
dft = cv2.dft(np.float32(img), flags= cv2.DFT_COMPLEX_OUTPUT)

# re arrange a fourier transform x by shifting the zero frequency
# component to the center of the array
# otherwise it starts with the top left of the image 
dft_shift = np.fft.fftshift(dft)

# magnitude of the function is 20 log(abs(f))
# for values that are 0 we may end up with intermidiate values for log
# so we can add 1 to the array to avoid seeing a warning 
magnitude_spect = 20* np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# circular HPF mask, center circle is 0, remove all ones
# can be used for edge detection because low frequency at center are blocked
# and only hiogh frequency are allowed, edges are highly frequency compnent 
"""
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)

mask = np.ones((rows, cols, 2), np.uint8)
r = 80   # plays vital role to edges
center = [crow, ccol]
x,y = np.ogrid[:rows, :cols]
mask_area = (x-center[0]) ** 2 + (y- center[1]) ** 2 <=r*r
mask[mask_area] = 0
"""


# Circular LPF mask, center circle is 1, remaining all zeros
# Only allows low frequency components - smooth regions
#Can smooth out noise but blurs edges.
#

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
r = 100
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 1

"""
# Band Pass Filter - Concentric circle mask, only the points living in concentric circle are ones
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
r_out = 80
r_in = 10
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
mask[mask_area] = 1
"""

# apply mask and inverse DFT: Multiply fourier transformed image (values)
#with the mask values. 
fshift = dft_shift * mask

#Get the magnitude spectrum (only for plotting purposes)
fshift_mask_mag = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

#Inverse shift to shift origin back to top left.
f_ishift = np.fft.ifftshift(fshift)

#Inverse DFT to convert back to image domain from the frequency domain. 
#Will be complex numbers
img_back = cv2.idft(f_ishift)

#Magnitude spectrum of the image domain
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
print(img_back.shape)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rgb_img_back = cv2.cvtColor(img_back, cv2.COLOR_BGR2RGB)

fig = plt.figure(figsize=(12, 12))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img)
ax1.title.set_text('Input Image')
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(magnitude_spect, cmap='gray')
ax2.title.set_text('FFT of image')
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(fshift_mask_mag, cmap='gray')
ax3.title.set_text('FFT + Mask')
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img_back)
ax4.title.set_text('After inverse FFT')
plt.show()


