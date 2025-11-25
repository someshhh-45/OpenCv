import cv2 as cv
import numpy as np  
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)
 
 # contour detection is used to detect or outline the shape of an object in an image 
 # outline of person
 #boundary of fruit
 #shape of an object
 #edges of polygon

 #steps
 #1. convert to grayscale
 #2. blur the image
 #3. canny edge detection   
 #4. find contours
 #5. draw contours

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blank=np.zeros(img.shape,dtype='uint8')
#cv.imshow('Blank',blank)



blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)

/*** RETR_LIST returns the numbers of contours 
 we can also use
RETR_TREE returns the hierarchy of like parent(outer contour) child(inner)
RETR_EXTERNAL returns only external contours
CHAIN_APPROX_NONE returns every poin(coordinate) in boundary similary 
CHAIN_APPROX SIMPLE returns start  and end ***/

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!')
cv.drawContours(blank,contours,-1,(0,255,0),1) #-1 means draw all contours , (0,255,0) is color green , 2 is thickness
cv.imshow('Contours Drawn',blank)



cv.waitKey(0)


