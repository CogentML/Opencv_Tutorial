import os

import cv2

img = cv2.imread(os.path.join('data', 'bear.jpg'))

img = cv2.imread(os.path.join('data', 'bird_resized.jpg'))


img_edge = cv2.Canny(img, 300, 400)

cv2.imshow('image', img)
cv2.imshow('edge', img_edge)
cv2.waitKey(0)