import cv2
img_file = "Images/img_2.jpg"

gray_img = cv2.imread(img_file, 0)
color_img = cv2.imread(img_file, 1)
# convert color image to RGB 
# color_rgb = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

print("Gray image shape: ",gray_img.shape)
print("Color image shape: ", color_img.shape)


cv2.imshow("Gray image", gray_img)
cv2.imshow("Color image BGR", color_img)
# cv2.imshow("Color image RGB", color_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()