# using scikit-image 
from skimage import io, img_as_float, img_as_ubyte

# reading an image 
img = io.imread('Images/img_1.jpg')

# getting shape of image
print("Shape of this image is: ", img.shape)

# printing image 
print('Original image: \n',img)

# converting image as float 
img2 = img_as_float(img)   # it scales image values between 0 and 1 with floating point numbers
print('After converting image into floating point: \n',img2)

# converting image as 8 bit image(original image)
img3 = img_as_ubyte(img2)
print('Floating point to original image(8-bit image): \n',img3)

######################################################################
# Using OpenCV
print('\n ======================== OpenCV ================================ ')
import cv2

c_img = cv2.imread("Images/img_1.jpg")
print('Shape of image: ',c_img)  # this reads as color image

# opencv reads images as BGR rather than RGB
# By default it read image as as color image 
# But if we want to read an image as grayscale then we need to read image this way
gray_img = cv2.imread("Images/img_1.jpg", 0)
print("Shape of gray image: ", gray_img.shape)

# And if we want to define as color image then we can write this way
color_img = cv2.imread("Images/img_1.jpg", 1)
print("Shape of color images: ", color_img.shape)

# converting BGR to RGB 
rgb_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)
print("Shape of cpnverted iamge: ", rgb_img.shape)
