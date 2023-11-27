import os

import cv2

img = cv2.imread(os.path.join("data", "bird_resized.jpg"))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img.shape)
cv2.imshow("BGR Bird", img)
cv2.imshow("RGB Bird", img_rgb)
cv2.imshow("Gray Bird", img_gray)
cv2.imshow("HSV Bird", img_hsv)
cv2.waitKey(0)