"""
About HSV images
"""
import cv2
from skimage import io
import matplotlib.pyplot as plt

img_file = "Images/img_3.jpg"
c_cv = cv2.imread(img_file, 1)
g_cv = cv2.imread(img_file, 0)

c_sk = io.imread(img_file, as_gray= False)
g_sk = io.imread(img_file, as_gray= True)

print("Shape of color image(OpenCV): ", c_cv.shape)
print("Shape of gray image(OpenCV): ", g_cv.shape)
print("Shape of color image(skimage): ", c_sk.shape)
print("Shape of gray image(skimage): ", g_sk.shape)

# splitting c_cv image into three chanel B,G,R
b, g, r = cv2.split(c_cv)

## Converting BGR to HSV image 
hsv_img = cv2.cvtColor(c_cv, cv2.COLOR_BGR2HSV)

# splitting HSV image into H,S,V channel
h,s,v = cv2.split(hsv_img)

# converting BRG image into LAB image
lab_img = cv2.cvtColor(c_cv, cv2.COLOR_BGR2LAB)
# splitting LAB image into three separate channel
l,a,b = cv2.split(lab_img)

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(3,4,1)
plt.imshow(b, cmap="gray")
ax1.title.set_text("B")

ax2 = fig.add_subplot(3,4,2)
plt.imshow(g, cmap= 'gray')
ax2.title.set_text("G")

ax3 = fig.add_subplot(3,4,3)
plt.imshow(r,cmap= 'gray')
ax3.title.set_text("R")

ax4 = fig.add_subplot(3,4,4)
plt.imshow(c_cv )
ax4.title.set_text("Original")

ax5 = fig.add_subplot(3,4,5)
plt.imshow(h, cmap="gray")
ax5.title.set_text("H")

ax6 = fig.add_subplot(3,4,6)
plt.imshow(s, cmap= 'gray')
ax6.title.set_text("S")

ax7 = fig.add_subplot(3,4,7)
plt.imshow(v, cmap= 'gray')
ax7.title.set_text("V")

ax8 = fig.add_subplot(3,4,8)
plt.imshow(c_cv )
ax8.title.set_text("Original")

ax9 = fig.add_subplot(3,4,9)
plt.imshow(l, cmap="gray")
ax9.title.set_text("L")

ax10 = fig.add_subplot(3,4,10)
plt.imshow(a, cmap= 'gray')
ax10.title.set_text("A")

ax11 = fig.add_subplot(3,4,11)
plt.imshow(b, cmap= 'gray')
ax11.title.set_text("B")

ax12 = fig.add_subplot(3,4,12)
plt.imshow(c_cv )
ax12.title.set_text("Original")

plt.show()

