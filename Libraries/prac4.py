import numpy as nm
import cv2 as cv

img=nm.zeros((512,512,3),nm.uint8)

cv.line(img,(0,0),(500,500),(255,0,0),5)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)


font = cv.FONT_HERSHEY_SIMPLEX
cv.waitKey(1)
cv.destroyAllWindows()