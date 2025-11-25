import cv2 as cv
img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)

#average blurring in this method we take the average of all the pixels under the kernel area and replace the central pixel with this average value
average=cv.blur(img,(3,3)) #(3,3) is kernel size
cv.imshow('Average Blurring',average)


#gaussian blurring it is similar to average blurring but here the weightage is given to the central pixels more than the outer pixels(average of weights is given to central pixel)
gaussian=cv.GaussianBlur(img,(3,3),0) #(3,3) is kernel size , 0 is sigma value(standard deviation in x direction)
cv.imshow('Gaussian Blurring',gaussian)

#median blurring in this method the central pixel is replaced with the median(middle value) of all the pixels under the kernel area.it is very effective in removing salt and pepper noise
median=cv.medianBlur(img,3) #3 is kernel size
cv.imshow('Median Blurring',median)

#bilateral blurring it is very effective in noise removal while keeping edges sharp.it is slower than the other blurring techniques
bilateral=cv.bilateralFilter(img,9,35,25) #9 is diameter of pixel neighborhood,35 is sigma color,25 is sigma space
cv.imshow('Bilateral Blurring',bilateral) #sigma color and sigma space determine how much the colors and space will be considered for blurring
cv.waitKey(0)   #lower sigma values means less blurring and higher sigma values means more blurring
#lower sigma space means that only pixels close to the central pixel will be considered for blurring and higher sigma space means that pixels far away from the central pixel will also be considered for blurring