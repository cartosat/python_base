import numpy;
import cv2 as v;

VSW=v.imread('pic.jpg',1)

v.imshow('pic.jpg',VSW)
key=v.waitKey(0)

if key==27:
    v.destroyAllWindows()


elif key==ord('s'):
    v.imwrite('pic.png',VSW)

