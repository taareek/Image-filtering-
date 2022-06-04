from skimage import io
img = io.imread("Images/img_1.jpg")

# importing filter librabires
from skimage import filters

# applying gaussian filter to original image 
gaussian_img = filters.gaussian(img, sigma= 2)
print(gaussian_img)

# save that image
dest_path = 'filtered/'
io.imsave(dest_path+ 'gaussian_img.jpg', gaussian_img)

# when we apply filter to image, it converts  to float 
# we should convert that filtered image into ubyte(8-bit) which  basically scaled values in  0-255  range
from skimage import img_as_ubyte
g_con = img_as_ubyte(gaussian_img)
io.imsave(dest_path+ 'gaussian_8bit.jpg', g_con)
# print(g_con)

###########################
###### OPenCV #############

import cv2
cv2.imwrite(dest_path+ 'gaussian_without_converting_opencv.jpg', g_con)

# we know opencv reads images as BGR pattern, that's we need to convert that into RGB
# otherwise we will lose information about original image
# now, converting BGR to RGB
g_rgb = cv2.cvtColor(g_con, cv2.COLOR_BGR2RGB)

# saving converted image
cv2.imwrite(dest_path+ 'gaussian_rgb_opencv.jpg', g_rgb)

#######################################
####### Using Matplotlib ##############

import matplotlib.pyplot as plt
# matplot reads as RGB pattern, so we don't need to convert 
# saving image using matplotlib
plt.imsave(dest_path+'gasussian_matplot.jpg', g_con)

# plotting image 
plt.imshow(g_con)
plt.show()


