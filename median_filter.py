from re import A
import matplotlib.pyplot as plt
import cv2
from skimage.filters import median
from skimage.morphology import disk

img_path = "Images/img_5.png"
img_path1 = "Images/img_3.jpg"

img = cv2.imread(img_path, 0)
img1 = cv2.imread(img_path1, 1)

# plt.imshow(img, cmap= 'gray')
# plt.show()

# median using cv2
c_img = cv2.medianBlur(img, 5)  # 3 is the kernel size

# median using skimage
s_img = median(img, disk(3), mode= 'constant', cval= 0.0)

fig = plt.figure(figsize=(12,12))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img, cmap= 'gray')
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(c_img,cmap= 'gray')
ax2.title.set_text("Using opencv")

ax3 = fig.add_subplot(1,3,3)
ax3.imshow(s_img, cmap= 'gray')
ax3.title.set_text("Using skimage")

plt.show()

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# median using cv2
c_img = cv2.medianBlur(img1, 5)  # 3 is the kernel size


# median using skimage
# s_img = median(img1, disk(3), mode= 'constant', cval= 0.0)

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
