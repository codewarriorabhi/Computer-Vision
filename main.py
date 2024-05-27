import cv2
import numpy

img = cv2.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\pexels.jpg",5)

img = cv2.resize(img, (800,700))

#img = cv2.flip(img,-1)

cv2.imshow("warriorr",img)

cv2.waitKey(0)


