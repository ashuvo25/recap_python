import cv2
import os
import numpy as np

img = cv2.imread(os.path.join("shuvo.jpeg"))
img = cv2.resize(img,(600,600))

img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# img = cv2.blur(img ,(5,5))
img  = cv2.Canny(img,50,100)
img = cv2.dilate(img, np.ones((5,5), dtype = np.uint8))
cv2.imshow('shuvo',img)
cv2.waitKey(0)