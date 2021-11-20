import cv2
import numpy as np
framewidth =640
frameheight =480

def empty(a):
    pass

im = cv2.VideoCapture("work/1.mp4")
im.set(3,framewidth)
im.set(4,frameheight)
im.set(10,150)

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("hue min","Trackbars",78,179,empty)
cv2.createTrackbar("hue max","Trackbars",87,179,empty)
cv2.createTrackbar("sat min","Trackbars",109,255,empty)
cv2.createTrackbar("sat max","Trackbars",212,255,empty)
cv2.createTrackbar("val min","Trackbars",86,255,empty)
cv2.createTrackbar("val max","Trackbars",255,255,empty)


while True:
    success , img =im.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("hue min","Trackbars")
    h_max = cv2.getTrackbarPos("hue max", "Trackbars")
    s_min = cv2.getTrackbarPos("sat min", "Trackbars")
    s_max = cv2.getTrackbarPos("sat max", "Trackbars")
    v_min = cv2.getTrackbarPos("val min", "Trackbars")
    v_max = cv2.getTrackbarPos("val max", "Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
