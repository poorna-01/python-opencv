import cv2
import numpy as np

def region_of_interest(image):
    polygons = np.array([[(13, 636), (1478, 719), (797,297)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask , polygons , 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


image = cv2.imread('s.PNG')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
canny = cv2.Canny(blur, 50, 150)
cropped_image = region_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

cv2.imshow('result',cropped_image)
cv2.waitKey(0)