import cv2
import numpy as np

cap = cv2.VideoCapture("time5.mp4")

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_white = np.array([0,0,0])
    up_white = np.array([0,0,255])

    mask = cv2.inRange(hsv, low_white, up_white)
    res = cv2.bitwise_and(frame, frame, mask= mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()