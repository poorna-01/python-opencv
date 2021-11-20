import cv2

cap = cv2.VideoCapture("work/l1.mp4")



while True:
    success , img =cap.read()
    imgR = cv2.resize(img,(1280,720))
    cv2.imshow("Cam",imgR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break