import cv2
import numpy as np
img1 = cv2.imread('ship.jpg',1)
img2 = cv2.imread('sun.jpg',1)
img1=cv2.resize(img1,(200,200),interpolation=cv2.INTER_AREA)
img2=cv2.resize(img2,(200,200),interpolation=cv2.INTER_AREA)
blend = cv2.addWeighted(img1,0.7,img2,0.5,0)
B, G, R = cv2.split(blend)
B1,G1,R1=cv2.split(img1)
B2,G2,R2=cv2.split(img2)

cv2.imshow('blended',blend)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('blue',B)
cv2.imshow('blue1',B1)
cv2.imshow('blue2',B2)
cv2.waitKey(0)
cv2.destroyAllWindows()