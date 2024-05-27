import cv2 as cv
import numpy as np
import os

img_list = os.listdir(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img")

for image in img_list:
    path = "C:\\Users\\Code-Warriorr\\Desktop\\Code2024\\Computer Vision\\Img"
    
    imga_name = path + "\\" + image
    imga_nam = cv.imread(imga_name)
    imga_nam = cv.resize(imga_nam,(250,200))
    
    cv.imshow("Abhishek Kumar",imga_nam)
    
    cv.waitKey(0)
cv.destroyAllWindows()