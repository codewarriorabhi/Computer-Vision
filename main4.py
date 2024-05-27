import cv2 as cv
import numpy as np
import os

list_name = os.listdir(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img")

for name in list_name:
    path = "C:\\Users\\Code-Warriorr\\Desktop\\Code2024\\Computer Vision\\Img"
    img_name = path + "\\" + name
    
    img = cv.imread(img_name)
    img = cv.resize(img,(800,600))
    
    cv.imshow("Abhishek",img)
    cv.waitKey(0)
    
cv.destroyAllWindows()