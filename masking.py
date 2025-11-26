import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Original Image',img)

blank=np.zeros(img.shape,dtype='uint8')
mask=cv.circle(blank.copy(),(img.shape[1]//2+45,img.shape[0]//2),100,(255,255,255),-1)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),(255,255,255),-1)
mask=cv.bitwise_or(mask,rectangle)
cv.imshow('Mask',mask)

masked=cv.bitwise_or(img,img,mask=mask[:,:,0])
cv.imshow('Masked Image',masked)

cv.waitKey(0)