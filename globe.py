import cv2
import glob

file_list = glob.glob('Images/*.*')
# print(file_list)

my_list = []

path = 'filtered/*.*'
dest_path = 'test/'

img_num = 0

for file in glob.glob(path):
    print(file)
    a = cv2.imread(file)
    my_list.append(a)

    c = cv2.cvtColor(a, cv2.COLOR_BGR2RGB)
    cv2.imwrite(dest_path+ 'converted_'+ str(img_num) + ".jpg", c)
    img_num += 1

    cv2.imshow('Color Image', c)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()

from matplotlib import pyplot as plt
plt.imshow(my_list[2])
plt.show()