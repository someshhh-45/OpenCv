import cv2 as cv
import numpy as np
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)
#translation is shifting the image along x and y axis withour changing its content
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]]) #0,1 1,0 are keep the image same
    dimensions=(img.shape[1],img.shape[0]) #width and height
    return cv.warpAffine(img,transMat,dimensions) #applying the transformation warpAffine function
# -x --> left
# -y --> up 
# +x --> right
# +y --> down
translated=translate(img,100,100)
cv.imshow('Translated',translated)

#rotation of image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2] # getting height and width of image
    if rotPoint is None:
        rotPoint=(width//2,height//2) # center of image
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0) # 1.0 is scale factor (zoom in or out of image)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions) #applying the transformation warpAffine function
rotated=rotate(img,-45) # rotating 45 degrees
cv.imshow('Rotated',rotated)
rotated_rotate=rotate(rotated,-45) # rotating -45 degrees
cv.imshow('Rotated -45',rotated_rotate)


#resizing image
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)   # INTER_CUBIC is for better quality
cv.imshow("resize",resized) 

#flipping image
flipped=cv.flip(img,-1)  # 0 for vertical , 1 for horizontal,-1 for both
cv.imshow("Flipped",flipped)    

#cropping
cropped=img[0:200,300:500]   # y axis from 0 to 200 and x axis from 300 to 500
cv.imshow('Cropped',cropped)    






cv.waitKey(0)