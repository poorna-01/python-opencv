import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(200,200),(0,0,255),5)
cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(255,255,0),5)
cv2.circle(img,(256,256),30,(0,255,0),5)
cv2.putText(img," OPENCV ",(50,250),2,cv2.FONT_HERSHEY_COMPLEX,(0,0,253),5)

cv2.imshow("area",img)

cv2.waitKey(0)