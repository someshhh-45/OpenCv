# edge cascading is done to detect or extract best edges after applying various filters like gaussian blur.
import cv2 as cv
import numpy as np  
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)  
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur) 
canny=cv.Canny(blur,125,175)   # 125 and 175 are min and max threshold values. for cosidering edges
                                # higher threshold value means strong edges
cv.imshow('Canny Edges',canny)
           # only strong edges reamin after canny edge detection noise is removed by gaussian blur


# to get back the original image from canny edges we use dilate and erode
dilated=cv.dilate(canny,(7,7),iterations=3)     # to increase the thickness of edges
cv.imshow('Dilated',dilated)  #(7,7) is the kernel size whic means size of brush for increasing thickness
eroded=cv.erode(dilated,(7,7),iterations=3)   # to decrease the thickness of edges
cv.imshow('Eroded',eroded)

resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)

# Cropping
cropped=img[0:200,200:500]   # y axis from 0 to 200 and x axis from 200 to 500
cv.imshow('Cropped',cropped)
cv.waitKey(0)