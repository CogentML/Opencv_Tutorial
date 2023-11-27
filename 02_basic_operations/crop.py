import os

import cv2

img = cv2.imread(os.path.join("data", "sample_image.png"))
croped_img = img[0:200, 100:200]

print(img.shape)
print(croped_img.shape)

# visulize
cv2.imshow('image', img)
cv2.imshow('resize image', croped_img)
cv2.waitKey(0)