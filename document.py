import cv2
import numpy as np

widthImg = 640
heightImg = 480


im = cv2.VideoCapture(0)
im.set(3,widthImg)
im.set(4,heightImg)
im.set(10,150)


def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img,(5,5),1)
    imgCanny = cv2.Canny(imgBlur,200,200)
    kernal = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny,kernal,iterations=2)
    imgThres = cv2.erode(imgDial,kernal,iterations=1)

    return imgThres

def getContours(img):
    biggest = np.array([])
    maxArea = 0
    contours,heirarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area =cv2.contourArea(cnt)
        if area>5000:
            #cv2.drawContours(imgContour , cnt , -1, (255,0,0) , 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
    return biggest

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew



def getWrap(img,biggest):
    biggest = reorder(biggest)
    print(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    return imgOutput


while True:

    success , img = im.read()
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres)
    # print(biggest)

    imgWraped = getWrap(img, biggest)

    cv2.imshow("original", imgWraped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

