import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.VideoCapture("video86.mp4")


while True:
    success , img =im.read()
    imgR = cv2.resize(img,(1280,720))
    lane_image = np.copy(imgR)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    kernal = np.ones((5, 5))
    imgDial = cv2.dilate(canny, kernal, iterations=3)
    imgThre = cv2.erode(imgDial, kernal, iterations=2)
    plt.imshow(imgThre)
    plt.show()
