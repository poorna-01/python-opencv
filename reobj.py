import cv2
import numpy as np
import fcont

path = 'Resource/rr.png'
scale = 3
wP = 210 * scale
hP = 297 * scale

while True:
    img = cv2.imread(path)

    img , conts = fcont.getContour(img,minArea=2000,filter=4)
    if len(conts) != 0:
        biggest =conts[0][2]
        #print(biggest)
        imgWrap = fcont.wrapImg(img,biggest,wP,hP)
        img2, conts2 = fcont.getContour(imgWrap, minArea=5000, filter=4,cThr=[50,50],draw=False)
        if len(conts) != 0:
            for obj in conts2:
                cv2.polylines(img2,[obj[2]],True,(0,255,0),2)
                nPoints = fcont.reorder(obj[2])
                nW = round((fcont.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                nH = round((fcont.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[1][0][0], nPoints[1][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                cv2.arrowedLine(img2, (nPoints[0][0][0], nPoints[0][0][1]),
                                (nPoints[2][0][0], nPoints[2][0][1]),
                                (255, 0, 255), 3, 8, 0, 0.05)
                x, y, w, h = obj[3]
                cv2.putText(img2, '{}cm'.format(nW), (x + 30, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,
                            (255, 255, 255), 2)
                cv2.putText(img2, '{}cm'.format(nH), (x - 10, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                            (255, 0, 255), 2)
        cv2.imshow('A4', img2)
        d = img2.shape
        print('img2',d)


    img = cv2.resize(img,(0,0),None,0.5,0.5)
    dimension = img.shape
    print(dimension)


    cv2.imshow('Original',img)
    cv2.waitKey(1)