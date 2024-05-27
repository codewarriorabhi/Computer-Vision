import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\astronaut-digital.jpg")
re_img = cv.resize(img,(300,300))

h = np.hstack((re_img,re_img,re_img))
v = np.vstack(((h,h)))

cv.imshow("stack",v)

cv.waitKey(0)
cv.destroyAllWindows()