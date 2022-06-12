"""
Total variation filter
"""
import cv2
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage.restoration import denoise_tv_chambolle

img = img_as_float(io.imread("Images/img_5.png"))

# plt.imshow(img, cmap= 'gray')
# plt.show()

# plotting histogram
plt.hist(img.flat, bins= 100, range=(0,1))
plt.show()

""""
denoise_tv_chambolle(image, weight= 0.1, eps= 0.0002, n_iter_max= 200, multichannel= False)
weight: The greater weight, the  more denoising(at the expense of fidility to input)
eps: Relative difference of the value of the cost function that determines the stop criterion
n_iter_max: Maxixmum number of iterations used for optimization 
"""
denoise_img = denoise_tv_chambolle(img, weight= 0.1, eps= 0.0002,
                                   n_iter_max= 200, multichannel= True)

# visualize
fig = plt.figure(figsize=(12,12))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(denoise_img, cmap= 'gray')
ax2.title.set_text("After applying Non-local means")

plt.show()