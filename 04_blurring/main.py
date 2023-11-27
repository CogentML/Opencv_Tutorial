import os

import cv2

img = cv2.imread(os.path.join("data", "bird_resized.jpg"))

kernel_size = 7

img_blur = cv2.blur(img, (kernel_size, kernel_size))
img_gaussian_blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), 5)
img_median_blur = cv2.medianBlur(img, kernel_size)

cv2.imshow("Bird", img)
cv2.imshow("img_blur", img_blur)
cv2.imshow("img_gaussian_blur", img_gaussian_blur)
cv2.imshow("img_median_blur", img_median_blur)
cv2.waitKey(0)