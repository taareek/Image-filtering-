import os

path = 'filtered/'
print(os.listdir(path))

for image in os.listdir(path):
    print(image)
    