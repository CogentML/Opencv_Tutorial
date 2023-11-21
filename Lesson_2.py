# # Read-Write-Visualize an Image

# import os

# import cv2

# # Path
# img_path = os.path.join("data", "sample_image.png")
# # print(img_path)

# # Reading an image
# img = cv2.imread(img_path)

# # Writing an image
# cv2.imwrite(os.path.join("data", "sample_image_out.png"), img)

# # Visualize an image
# cv2.imshow("Image", img)

# # Wait for a key press
# # cv2.waitKey(0) # Press any key to exit the image preview
# cv2.waitKey(1000) # image preview will be displayed for 1000 milliseconds

##---------------------------------------------------------

# Visualize a video

import os

import cv2

video_path = os.path.join("data", "sample_video.mp4")

# read video
video = cv2.VideoCapture(video_path)

# visualize video
ret = True

while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow("Video", frame)
        cv2.waitKey(1)
