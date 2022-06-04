from skimage import io
img = io.imread("Images/img_3.jpg")
print("Shape of image: ",img.shape)

# visualize image
# io.imshow(img)

# Another way using ImageViewer
from skimage import data
from skimage.viewer import ImageViewer

# image = data.coins()
# viewer = ImageViewer(image)
# viewer.show()

image = img
viewer = ImageViewer(image)
viewer.show()

#############################
# using matplolib
import matplotlib.pyplot as plt
plt.imshow(img)
plt.show()

img_gray = io.imread("Images/img_3.jpg", as_gray= True)
# subplotting
fig = plt.figure(figsize=(10,10))

ax1 = fig.add_subplot(2,2,1)
ax1.imshow(img_gray, cmap= 'hot')
ax1.title.set_text("cmap: hot")

ax1 = fig.add_subplot(2,2,2)
ax1.imshow(img_gray, cmap= 'jet')
ax1.title.set_text("cmap: jet")

ax1 = fig.add_subplot(2,2,3)
ax1.imshow(img_gray, cmap= 'gray')
ax1.title.set_text("cmap: gray")

ax1 = fig.add_subplot(2,2,4)
ax1.imshow(img_gray, cmap= 'Blues')
ax1.title.set_text("cmap: Blues")
plt.show()


