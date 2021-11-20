import cv2
import numpy as np

im = cv2.VideoCapture("time5.mp4")


cr_points = np.float32([[590,530],[920,530],[1100,720],[200,720]])

width = 1280
height = 720
img_mat = np.float32([[0,0],[width,0],[width,height],[0,height]])

'''def display_lines(img, lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)
    return line_image'''


def region_of_interest(canny):
    height = img.shape[0]
    width = img.shape[1]
    mask = np.copy(img)
    triangle = np.array([[
        [400, height],
        [1200, height],
        [850, 580],
        [590,580]
        ]], np.int32)
    cv2.fillPoly(mask,triangle, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

while True:
    success , img =im.read()
    #roi = region_of_interest(img)
    #cv2.imshow("roi",roi)


    matrix = cv2.getPerspectiveTransform(cr_points,img_mat)
    img_trans = cv2.warpPerspective(img , matrix,(width,height))
    cv2.imshow("bird",img_trans)

    '''
    hsv = cv2.cvtColor(img_trans,cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 168])
    upper_white = np.array([172,111,255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(img_trans, img_trans, mask= mask )
    cv2.imshow("white",res)

    canny = cv2.Canny(res, 50, 150)
    cv2.imshow("canny",canny)
    line_image = np.copy(res) * 0
    lines = cv2.HoughLinesP(canny, 1, np.pi/180, 40, minLineLength=50, maxLineGap=20 )
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
    line_edges = cv2.addWeighted(img_trans,0.8,line_image,1,0)
    cv2.imshow("line",line_edges)

    cv2.imshow("res",line_edges)


    combo_image = cv2.addWeighted(img, 0.8, line_image, 1, 1)
    cv2.imshow("gg",combo_image)'''


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break