import cv2
import matplotlib.pyplot as plt
from skimage import io
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage import filters
from skimage.color import rgb2gray

img_file= "Images/monalisa.jpg"

img = io.imread(img_file)
plt.imshow(img)
plt.show()

img_2 = io.imread(img_file, as_gray= True)
plt.imshow(img_2, cmap= 'gray')
plt.show()

# applying sobel filter on our imported image 
try_sobel = filters.sobel(img_2)
plt.imshow(try_sobel, cmap='gray')
plt.show()

"""
If we use updated version of skimage we can apply sobel on color images
in my case, I have loaded image as gray to apply sobel. But if we apply 
skimage's sobel on a color image it will not give us expected output or 
may fail as it is a gray filter. so we need to use different techniques
which is shown below
"""

# Two ways to apply gray filters on color image 
# 1. Separate R, G, B and apply filters each channel and combine them; but it produce bad result
# 2. Convert RGB to HSV then apply to V channel and put it back to HSV and convert into RGB

@adapt_rgb(each_channel)
def sobel_each(image):
    return filters.sobel(image)

@adapt_rgb(hsv_value)
def sobel_hsv(image):
    return filters.sobel(image)

each_channel_img = sobel_each(img)
# print(each_channel_img.shape)

hsv_value_img = sobel_hsv(img)

plt.imshow(each_channel_img)
plt.show()

plt.imshow(hsv_value_img)
plt.show()