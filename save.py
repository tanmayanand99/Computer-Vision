import numpy as np
import cv2

img=cv2.imread('image.jpg')
img=cv2.imwrite('image.png', img)

cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()