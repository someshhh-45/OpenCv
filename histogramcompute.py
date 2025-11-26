import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)
blank=np.zeros(img.shape,dtype='uint8')
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,(255,255,255),-1)
#cv.imshow('Mask',circle[:,:,0])
mask=cv.bitwise_and(img,img,mask=circle[:,:,0])
cv.imshow('Masked Image',mask)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)


#histogram=cv.calcHist([gray],[0],mask[:,:,0],[256],[0,256])
plt.figure()    
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Color Histogram')

colors=('b','g','r')
for i,col in enumerate(colors):
    histogram=cv.calcHist([mask],[i],circle[:,:,0],[256],[0,256])
    plt.plot(histogram,color=col)
    plt.xlim([0,256])



plt.show()



cv.waitKey(0)
