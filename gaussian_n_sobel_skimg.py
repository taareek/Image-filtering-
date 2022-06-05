import matplotlib.pyplot as plt
from skimage import io 
from skimage.filters import gaussian, sobel

# reading image
img = io.imread("Images/img_3.jpg")
plt.imshow(img)
plt.title("Original image")
plt.show()

# Applying gaussian filter
g_img = gaussian(img, sigma= 2, mode= 'constant', cval= 0.0)
plt.imshow(g_img)
plt.title('After applying gaussian filter')
plt.show()

# Applying sobel 
s_img = io.imread("Images/img_3.jpg", as_gray= True)
s_img = sobel(s_img)
plt.imshow(s_img, cmap='gray')
plt.title("After applying sobel filter")
plt.show()