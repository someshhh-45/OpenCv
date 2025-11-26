#thresholding converts an image into binary image , either black or white , pixel value either 0 or 255
#threshold value is used to classify pixel values if > threshold value then pixel value is set to 255(white) else set to min value(0) (black)
import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original Image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)
#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)
#inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholding', thresh_inv)
#adaptive thresholding
#here threshold value is calculated for smaller regions of image so we get different threshold values for different regions
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3) # 11 is block size (size of neighborhood area) , 3 is constant subtracted from mean
cv.imshow('Adaptive Thresholding', adaptive_thresh)
cv.waitKey(0)