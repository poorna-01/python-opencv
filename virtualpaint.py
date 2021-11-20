import cv2
import numpy as np
framewidth =640
frameheight =480

im = cv2.VideoCapture(0)
im.set(3,framewidth)
im.set(4,frameheight)
im.set(10,150)

myColors = [[78,109,86,87,212,255]]

myColorValue =[[51,255,51]]     #BGR

mypts = []         #x,y,colorId

def findColor(img,myColors,myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    x,y = getContours(mask)
    cv2.circle(Imgresult,(x,y),10,myColorValue[count],cv2.FILLED)
    if x!=0 and y!=0:
        newPoints.append([x,y,count])
    #cv2.imshow("img",mask)
    return newPoints

def getContours(img):
    contours,heirarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult , cnt , -1, (255,0,0) , 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return  x+w//2,y

def drawOnCanvas(mypts,myColorValue):
    for point in mypts:
        cv2.circle(Imgresult, (point[0], point[1]), 10, myColorValue[point[2]], cv2.FILLED)


while True:
    success , img =im.read()
    Imgresult = img.copy()
    newPoints = findColor(img,myColors,myColorValue)
    if len(newPoints)!=0:
        for newP in newPoints:
            mypts.append(newP)
    if len(mypts)!=0:
        drawOnCanvas(mypts,myColorValue)

    cv2.imshow("Cam",Imgresult )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break