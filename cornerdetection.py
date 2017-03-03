import cv2
import numpy as np

img = cv2.imread('opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corner = cv2.goodFeaturesToTrack(gray,100,0.01,10)
corner = np.int0(corner)

for corners in corner:
	x, y = corners.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)
	
cv2.imshow('corner',img)
cv2.waitKey()