import numpy as np
import cv2

pic=np.zeros((500,500,3), dtype='uint8')
cv2.rectangle(pic, (0,0), (500,150), (125,345,23), 3, lineType=8, shift=0)
cv2.imshow('black.jpg', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()