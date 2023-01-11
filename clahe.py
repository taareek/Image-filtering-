"""
This script is used for histogram equalization and contrast limited adaptive histogram equalization (CLAHE)
"""
import cv2
import matplotlib.pyplot as plt
from skimage import io

img_file = cv2.imread("Images/img_3.jpg", 1)
# plt.imshow(img_file)
# plt.show()
# getting original image
rgb_img = cv2.cvtColor(img_file, cv2.COLOR_BGR2RGB)

# converting to image to LAB color space so CLAHE can be applied to luminance
lab_img = cv2.cvtColor(img_file, cv2.COLOR_BGR2LAB)

fig = plt.figure(figsize=(8,8))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(img_file)
ax1.title.set_text("BGR image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(rgb_img)
ax2.title.set_text("RGB image: Original")

ax3 = fig.add_subplot(1,3,3)
ax3.imshow(lab_img)
ax3.title.set_text("LAB image")

fig.suptitle('BGR, RGB and LAB image', fontsize=16)
plt.show()

# splitting LAB image into l,a, b channel
l,a,b = cv2.split(lab_img)

fig = plt.figure(figsize=(8,8))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(l)
ax1.title.set_text("L")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(a)
ax2.title.set_text("A")

ax3 = fig.add_subplot(1,3,3)
ax3.imshow(b)
ax3.title.set_text("B")

fig.suptitle('Three channel of LAB image ', fontsize=16)
plt.show()

# plotting histogram of LAB images
fig = plt.figure(figsize=(8,8))

ax1= fig.add_subplot(1, 3, 1)
ax1.hist(l.flat, bins= 100, range=(0,255))
ax1.title.set_text("L histogram")

ax2= fig.add_subplot(1,3,2)
ax2.hist(a.flat, bins= 100, range=(0,255))
ax2.title.set_text("A histogram")

ax3 = fig.add_subplot(1,3,3)
ax3.hist(b.flat, bins= 100, range=(0,255))
ax3.title.set_text("B histogram")

fig.suptitle('Histogram for LAB ', fontsize=16)
plt.show()

# plotting histogram for original image
# plt.hist(rgb_img.flat, bins = 300, range=(0,255))
# plt.show()

# applying histogram equalization to the L channel
l_equ = cv2.equalizeHist(l)

# plotting histogram of L chanel before and after histogram equalization
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 2, 1)
ax1.hist(l.flat, bins= 100, range=(0,255))
ax1.title.set_text("Before equalization")

ax2= fig.add_subplot(1,2,2)
ax2.hist(l_equ.flat, bins= 100, range=(0,255))
ax2.title.set_text("After equalization")

fig.suptitle('Histogram of L channel ', fontsize=16)
plt.show()

# plotting image of L chanel before and after histogram equalization
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 2, 1)
ax1.imshow(l)
ax1.title.set_text("Before equalization")

ax2= fig.add_subplot(1,2,2)
ax2.imshow(l_equ)
ax2.title.set_text("After equalization")

fig.suptitle('Image of L channel', fontsize=16)
plt.show()

# combine the equalized image L channel back with A and B channel
equ_lab = cv2.merge((l_equ, a, b))

# plotting Lab image before and after histogram equalization
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 2, 1)
ax1.imshow(lab_img)
ax1.title.set_text("Before equalization")

ax2= fig.add_subplot(1,2,2)
ax2.imshow(equ_lab)
ax2.title.set_text("After equalization")

fig.suptitle('LAB image before and after equalization', fontsize=16)
plt.show()

# converting LAB image back to color
equ_col = cv2.cvtColor(equ_lab, cv2.COLOR_LAB2RGB)   # equalized method

# applying clahe to L channel
clahe = cv2.createCLAHE(clipLimit= 3.0, tileGridSize=(8,8))
clahe_img = clahe.apply(l)

# plotting histogram after applying clahe on L 
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 2, 1)
ax1.hist(l_equ.flat, bins= 100, range=(0,255))
ax1.title.set_text(" equalization")

ax2= fig.add_subplot(1,2,2)
ax2.hist(clahe_img.flat, bins=100, range=(0,255))
ax2.title.set_text("CLAHE on equalized")

fig.suptitle("L channel's histogram for equalization and CLAHE", fontsize=16)
plt.show()

# plotting L channel image after equalization and CLAHE 
# plotting Lab image before and after histogram equalization
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 2, 1)
ax1.imshow(l_equ)
ax1.title.set_text(" equalization")

ax2= fig.add_subplot(1,2,2)
ax2.imshow(clahe_img)
ax2.title.set_text("CLAHE on equalized")

fig.suptitle("L channel's histogram for equalization and CLAHE", fontsize=16)
plt.show()

# now combining clahe L, A and B
f_clahe_img = cv2.merge((clahe_img, a, b))
clahe_col = cv2.cvtColor(f_clahe_img, cv2.COLOR_LAB2RGB)

# Now we will plot original image, histogram equalized image and CLAHE image
fig = plt.figure(figsize=(10,10))

ax1= fig.add_subplot(1, 3, 1)
ax1.imshow(rgb_img)
ax1.title.set_text("Original image")

ax2= fig.add_subplot(1,3,2)
ax2.imshow(equ_col)
ax2.title.set_text("Histogram eualization")

ax3 = fig.add_subplot(1,3,3)
ax3.imshow(clahe_col)
ax3.title.set_text("CLAHE")

fig.suptitle('Original image alongwith two filters ', fontsize=16)
plt.show()