import matplotlib.pyplot as plt
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean

img = io.imread('Images/img_3.jpg')
print("Original image shape: ", img.shape)
# print(img)
plt.imshow(img)
plt.title("Original image")
plt.show()

# lab_img = color.rgb2lab(img)
# plt.imshow(lab_img)
# plt.show()

# resclaing image 
rescale_img = rescale(img, 0.25, anti_aliasing= False)
print("Resclaed image shape: ", rescale_img.shape)

# Resizing image 
resized_img = resize(img, (200,200), anti_aliasing= True)
print('Resized image shape: ',resized_img.shape)
plt.imshow(resized_img)
plt.title("Resized image")
plt.show()

# down-scaling image 
d_scale_img =  downscale_local_mean(img, (4, 3))
print("Down scaled image shape: ", d_scale_img.shape)
plt.imshow(d_scale_img)
plt.title("downsclaed image ")
plt.show()
