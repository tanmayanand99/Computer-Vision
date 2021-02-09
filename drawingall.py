import numpy as np
import cv2

pic=np.zeros((500,500,3), dtype='uint8')

cv2.rectangle(pic, (0,0), (500,150), (255,0,0), 3)

cv2.putText(pic,'Saumya',(100,100), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0), 3)

cv2.circle(pic, (250,250), 50, (0,0,255), 4)
cv2.circle(pic, (230,225),5, (255,255,255), 3)
cv2.circle(pic, (270,225),5, (255,255,255), 3)
cv2.line(pic, (200,255), (300,255), (0,255,0), 3)
cv2.imshow('Saumya',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()