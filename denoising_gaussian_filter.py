"""
In this script, I am using an image with salt and pepper noise
as original image. And I will apply both scikit learn's skimage 
and OpemCV's cv2 approaches to implement gaussian blur for 
removing the noise

"""

import cv2
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage.filters import gaussian

img_path = "Images/img_5.png"
img = io.imread(img_path)
f_img = img_as_float(img)
# here skimage reads as BGR,if you have color image then uncomment next cell
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(rgb_img)
# plt.show()

# gaussian using cv2 
c_img = cv2.GaussianBlur(img, (5,5), 3, borderType= cv2.BORDER_CONSTANT)

# gaussian using skimage 
s_img = gaussian(img, sigma= 3, mode= 'constant', cval= 0.0)

fig = plt.figure(figsize=(12,12))

ax1 = fig.add_subplot(1,3,1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("Original Image")

ax1 = fig.add_subplot(1,3,2)
ax1.imshow(c_img, cmap= 'gray')
ax1.title.set_text("Gaussian using opencv")

ax1 = fig.add_subplot(1,3,3)
ax1.imshow(s_img, cmap= 'gray')
ax1.title.set_text("Gaussian using skimage")
plt.show()