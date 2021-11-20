import cv2

nPlateCascade = cv2.CascadeClassifier("Resource/haarcascade_russian_plate_number.xml")

widthImg = 640
heightImg = 480
minArea = 500
color = (255,0,255)
count = 0


im = cv2.VideoCapture(0)
im.set(3,widthImg)
im.set(4,heightImg)
im.set(10,150)

while True:
    success , img =im.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlate = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)


    for (x, y, w, h) in numberPlate:
        area =w*h
        if area>minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)



    cv2.imshow("Cam",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resource/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"scanned",(150,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1
