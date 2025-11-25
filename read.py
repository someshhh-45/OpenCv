import cv2 as cv
#img = cv.imread('Resources/Photos/cat_large.jpg')
#cv.imshow('Cat', img)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'): press d to stop
            break
    else:
        break
capture.release()
cv.destroyAllWindows()


