import os

import cv2

img = cv2.imread(os.path.join("data", "sample_image.png"))
resize_img = cv2.resize(img, (695, 345)) # here we have to define width and then height

print(img.shape)
print(resize_img.shape)

# visulize
cv2.imshow('image', img)
cv2.imshow('resize image', resize_img)
cv2.waitKey(0)