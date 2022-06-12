"""
Non-local means filter
This is commonly used in CT, MRI and Microscopic images 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma

img_file = img_as_float(io.imread("Images/img_5.png", as_gray=False))

# plt.imshow(img_file)
# plt.show()

# getting sigma estimation
est_sigma = np.mean(estimate_sigma(img_file, multichannel= True))

# applying non-local means filter

denoise_img = denoise_nl_means(img_file, h= 2.15* est_sigma,
                                fast_mode= True,
                                patch_size= 5,
                                patch_distance= 3,
                                multichannel= True)
# print(denoise_img)

# denoise_img is in float format, if we want to save this image then we need to convert this into 8-bit
from skimage import img_as_ubyte
img_ubyte = img_as_ubyte(denoise_img)
# print(img_ubyte)

# visualize
fig = plt.figure(figsize=(12,12))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img_file)
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(denoise_img)
ax2.title.set_text("After applying Non-local means")

plt.show()


