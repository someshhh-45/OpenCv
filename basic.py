import cv2 as cv
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)
# converting to grayscale
#gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)
# blurring
blur=cv.GaussianBlur(img,(21,21),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)