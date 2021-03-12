import cv2
import numpy as np #image operations
img=cv2.imread('disha.jpg',1)
img[55,55]=[255,255,255]
px=img[55,55]
img[100:150,100:150]=[255,255,255]
disha_face=img[37:111,107:194]
img[0:74,0:87]=disha_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
