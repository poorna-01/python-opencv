import cv2

c=cv2.imread("Resource/lena.jpg")
print(c.shape)

imgResize = cv2.resize(c,(1000,500))
print(imgResize.shape)

imgCrop = imgResize[0:200,200:500]


cv2.imshow("original", c)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped Image", imgCrop)
cv2.waitKey(0)