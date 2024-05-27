import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\spider-man.png")

re_img = cv.resize(img,(1100,700))

cv.imshow("abhi", re_img)
cv.waitKey(0)


#v = np.array([[1,2,1,2,],[1,2,1,2]])


