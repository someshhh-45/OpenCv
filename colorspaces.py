import cv2 as cv
import matplotlib.pyplot as plt 
#color spaces : BGR, GRAY, HSV,yCrCb, LAB, RGB
#for detecting colors in an image HSV is most useful
#for face detection yCrCb is most useful
#for detecting objects in different lighting conditions LAB is most useful(brighten colors separates lighting)
#for detceting edges and shapes GRAY is most useful (color is not important here)




img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)

plt.imshow(img) # BGR to RGB conversion needed for correct color display
plt.show()
# converting to grayscale   
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
# converting to HSV color space
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
# converting to LAB color space
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
plt.show()


cv.waitKey(0)   