import numpy as num
import cv2 as cv

cap=cv.VideoCapture('swap.mp4')

while(cap.isOpened()):
    ret, frame=cap.read()
    col=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',col)
    if cv.waitKey(1) &0xFF==ord('q') :
        break
cap.release()
cv.destroyAllWindows()
