import cv2 as cv
import numpy as np
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

#blank[:] = 0, 255, 0
#cv.imshow('Green', blank)
#cv.waitKey(0)

""" cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=-1)
cv.imshow("Rectangle", blank)
cv.circle(blank, (250, 250),40, (255, 0, 255), thickness=-1)
cv.imshow("Circle", blank) """
cv.putText(blank,'Hello CV',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)
cv.destroyAllWindows()