import os

import cv2

# read image
image_path = os.path.join("data", "sample_image.png")

img = cv2.imread(image_path)

print(img.shape)


# write image
# cv2.imwrite("data/sample_image_copy.png", img)
cv2.imwrite(os.path.join("data", "sample_image_copy.png"), img)

# visualize image
cv2.imshow("image", img)
cv2.waitKey(0)