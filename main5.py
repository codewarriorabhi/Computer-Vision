import cv2 as cv
import numpy as np

imgage = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\spider-man.png")
imgage2 = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\astronaut-digital.jpg")
img = cv.resize(imgage,(150,100))
img2 = cv.resize(imgage2,(150,100))

h =  np.hstack((img,img2,img,img2))
v = np.vstack((h,h,h))

cv.imshow("Abhishek",v)

cv.waitKey(0)
cv.destroyAllWindows()