import cv2

# read webcam
webcam = cv2.VideoCapture(0)

# visualize the webcam

while True:
    # read the webcam
    ret, frame = webcam.read()

    # show the webcam
    cv2.imshow('Webcam', frame)

    # check if the user pressed the 'q' key
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()