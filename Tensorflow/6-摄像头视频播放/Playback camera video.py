import cv2
import sys
import datetime as dt
from time import sleep

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame
    ret, frame = video_capture.read()

    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When all shit is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

