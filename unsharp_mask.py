# usharped = original + amount * (original - blurred)

from skimage import io, img_as_float
from skimage.filters import unsharp_mask
from skimage.filters import gaussian

import matplotlib.pyplot as plt
import cv2

img = io.imread("Images/img_3.jpg", as_gray= True)
print(img.shape)
# plt.imshow(img)
# plt.show()

# converting image as float
f_img = img_as_float(img)
# print(f_img)

# applying gaussian filter to our image
g_img = gaussian(img, sigma= 2, mode= 'constant', cval= 0.0)
# plt.imshow(g_img)
# plt.show()

img_2 = (f_img - g_img) * 2
# making unsharp
unsharp_img = img_2 + f_img

fig = plt.figure(figsize= (10, 8))
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("Original gray image")

ax1 = fig.add_subplot(2,2,2)
ax1.imshow(g_img, cmap= 'gray')
ax1.title.set_text("gaussian blured image")

ax1 = fig.add_subplot(2,2,3)
ax1.imshow(img_2, cmap= 'gray')
ax1.title.set_text("(gaussian blured image - original image) * 2")

ax1 = fig.add_subplot(2,2,4)
ax1.imshow(unsharp_img, cmap= 'gray')
ax1.title.set_text("Unsharp image")

plt.show()

#### Using built in function 
unsharp_img1 = unsharp_mask(img, radius= 3, amount= 2)  # radius= amount of blurring ; amount= multiplication factor

fig1 = plt.figure(figsize= (8,8))
ax1 = fig1.add_subplot(1,2,1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("original image")

ax2 = fig1.add_subplot(1,2,2)
ax2.imshow(unsharp_img1, cmap= 'gray')
ax2.title.set_text("Unsharped image")
plt.show()

# trying on color image 
c_img = "Images/img_3.jpg"
c_img = io.imread(c_img)

unsharp_img2 = unsharp_mask(c_img, radius= 3, amount= 2)   

fig2 = plt.figure(figsize= (8,8))
ax1 = fig2.add_subplot(1,2,1)
ax1.imshow(c_img, cmap= 'gray')
ax1.title.set_text("original image")

ax2 = fig2.add_subplot(1,2,2)
ax2.imshow(unsharp_img2, cmap= 'gray')
ax2.title.set_text("Unsharped image")
plt.show()
