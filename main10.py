# Mark line on face 

import cv2 as cv

addr = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\Personal\CV_Photo_1.jpg")
addr = cv.resize(addr,(600,700))
img = addr

new_line = cv.line(
    img,
    pt1 = (100,50),
    pt2 = (500,50),
    color = (0,0,255),
    thickness = 4,
    lineType = 16)


cv.imshow("abhishek",new_line)

cv.waitKey(0)
cv.destroyAllWindows()