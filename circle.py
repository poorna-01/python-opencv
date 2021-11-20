import cv2
import numpy as np

path = 'rr.png'
scale = 3
wP = 210 *scale
hP = 297 *scale

def getContours(img,cThr=[100,100],showCanny=False,minArea=1000,filter = 0,draw = False):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,cThr[0],cThr[1])
    kernal = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernal,iterations=3)
    imgThre = cv2.erode(imgDial,kernal,iterations=2)
    if showCanny:cv2.imshow('Canny',imgThre)
    detected = cv2.HoughCircles(imgThre,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)
    if detected is not None:
        for pt in detected[0,:]:
            cv2.circle(img,(a,b0,r,(o,255,0),2))
            cv2.circle(img,(a,b),1,(0,0,255),3)
            cv2.imshow("Detect",img)

    contours,hiearchy = cv2.findContours(imgThre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    finalContours = []

    for i in contours:
        area = cv2.contourArea(i)
        if area >minArea:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            bbox = cv2.boundingRect(approx)
            if filter >0 :
                if len(approx) == filter:
                    finalContours.append([len(approx),area,approx,bbox,i])
            else:
                finalContours.append([len(approx),area,approx,bbox,i])


    finalContours = sorted(finalContours,key = lambda x:x[1] , reverse=True)
    if draw:
        for con in finalContours:
            cv2.drawContours(img,con[4],-1,(0,0,255),3)

    return img, finalContours

def reorder(myPoints):
    print(myPoints.shape)
    myPointsNew = np.zeros_like(myPoints)
    myPoints = myPoints.reshape((4,2))
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew


def wrapImg(img,points,w,h):
    #print(points)
    points = reorder(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgWrap = cv2.warpPerspective(img,matrix,(w,h))


    return imgWrap




img = cv2.imread(path)
img,cont = getContours(img,minArea=50000,filter = 4)
if len(cont) != 0:
    biggest = cont[0][2]
    #print(biggest)
    imgWrap = wrapImg(img,biggest,wP,hP)
    img2 , cont2 = getContours(imgWrap, minArea=5000, filter=4,cThr=[50,50],draw=False)
    cv2.imshow('A4', imgWrap)



cv2.imshow('Original',img)
cv2.waitKey(0)