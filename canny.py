import numpy as np
import cv2

pic=cv2.imread('image.jpg')

thresholdval1=100
thresholdval2=150

canny=cv2.Canny(pic, thresholdval1, thresholdval2)

cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()