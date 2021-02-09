import numpy as np
import cv2

pic=cv2.imread('taj.jpg')

kernel=3

median=cv2.medianBlur(pic, kernel)

cv2.imshow('median blur', median)
cv2.waitKey(0)
cv2.destroyAllWindows()