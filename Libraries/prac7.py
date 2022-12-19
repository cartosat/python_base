import cv2 as cv
import numpy as np

def nothing(x):
    pass

img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('color')

cv.createTrackbar('R','color',0,255,nothing)
cv.createTrackbar('G','color',0,255,nothing)
cv.createTrackbar('B','color',0,255,nothing)

switch='0:OFF \n1:ON'
cv.createTrackbar('switch','color',0,1,nothing)

while(1):
    cv.imshow('color',img)
    k=cv.waitKey(1)& 0xFF
    if k==27:
        break

    r=cv.getTrackbarPos('R','color')
    g=cv.getTrackbarPos('G','color')
    b=cv.getTrackbarPos('B','color')
    s=cv.getTrackbarPos('switch','color')

    if s==0:
        img[:]=0

    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()