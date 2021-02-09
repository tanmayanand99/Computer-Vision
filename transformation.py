import numpy as np
import cv2

pic=cv2.imread('image.jpg')

cols=pic.shape[1]
rows=pic.shape[0]


M=np.float32([[1,0,100],[0,1,100]])
shifted=cv2.warpAffine(pic, M, (cols,rows))

cv2.imshow('transform',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()