import matplotlib.pyplot as plt
import cv2
from skimage.restoration import denoise_bilateral

img_path = "Images/img_5.png"
img_path1 = "Images/img_3.jpg"

img = cv2.imread(img_path, 0)
img1 = cv2.imread(img_path1, 1)

# coverting image to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# plt.imshow(img1)
# plt.show()

# applying biliteral filter using opencv
c_img = cv2.bilateralFilter(img, 3, 30, 200, borderType= cv2.BORDER_CONSTANT)

"""
    img = img
    d = diameter of each pixel neighborhood used during filters
    sigmaColor = sigma gray/ color space
    sigmaSpace = Large value means farther pixels influence by each other
"""

# skimage is very slow, it take 5-6 minutes to process the image, better don't try this, use opencv
# using skimage
# s_img = denoise_bilateral(img, sigma_color= 0.5, sigma_spatial=15, multichannel= True)

# visualize
fig = plt.figure(figsize=(12,12))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(c_img,cmap= 'gray')
ax2.title.set_text("Using opencv")

# ax3 = fig.add_subplot(1,3,3)
# ax3.imshow(s_img, cmap= 'gray')
# ax3.title.set_text("Using skimage")

plt.show()


# applying biliteral filter using opencv
c_img = cv2.bilateralFilter(img1, 3, 30, 200, borderType= cv2.BORDER_CONSTANT)

# visualize
fig = plt.figure(figsize=(12,12))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img1, cmap= 'gray')
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(c_img,cmap= 'gray')
ax2.title.set_text("Using opencv")

# ax3 = fig.add_subplot(1,3,3)
# ax3.imshow(s_img, cmap= 'gray')
# ax3.title.set_text("Using skimage")

plt.show()