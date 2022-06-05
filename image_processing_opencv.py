import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Images/img_3.jpg', 1)  # 1 means color image 
print("original image shape: ", img.shape)

# resizing image 
resize_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_CUBIC)  
print('Resized image shape: ',resize_img.shape)

# cv2.imshow('original image',img)
# cv2.imshow('Resized image: ', resize_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# top left RGB value
top_left = img[0, 0]
print("Top left value: ", top_left)

# getting chanel wise image
blue = img[:,:, 0]
green = img[:,:,1]
red = img[:,:, 2]

print('Blue shape: ', blue.shape)
print("Green Shape: ", green.shape)
print("Red shape: ", red.shape)

# cv2.imshow('original image',img)
# cv2.imshow("Blue image: ", blue)
# cv2.imshow("Red image: ", red)
# cv2.imshow("Green image: ", green)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# another way to split image chanel
b, g, r = cv2.split(img)
print(b.shape)
print(g.shape)
print(r.shape)

# merged images 
merged_img = cv2.merge((b,g, r))
print("Merged image shape: ", merged_img.shape)

# cv2.imshow('Mergerd image (BGR)',merged_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Cany edge detector
g_img = "Images/img_3.jpg"
g_img = cv2.imread(g_img, 0)
print("Gray image shape: ", g_img.shape)

canny_img = cv2.Canny(g_img, 100, 200)
cv2.imshow('original gray image',g_img)
cv2.imshow("Canny edge detector", canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()