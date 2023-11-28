import os

import cv2

img = cv2.imread(os.path.join("data", "whiteboard.png"))

print(img.shape)

# line
cv2.line(img, (150,200), (300, 400), (0,255,0), 5)

# rectangle
# cv2.rectangle(img, (100,200), (300, 400), (0,0,255), cv2.FILLED)
# cv2.rectangle(img, (100,200), (300, 400), (0,0,255), -1)
cv2.rectangle(img, (100,200), (300, 400), (0,0,255), 5)

# circle
cv2.circle(img, (400,100), 50, (255,0,0), 5)

# text
cv2.putText(img, "Hello World", (100,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
cv2.imshow("Output", img)
cv2.waitKey(0)