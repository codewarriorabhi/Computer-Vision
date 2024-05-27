import cv2 as cv
import os

img_list = os.listdir(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img")

for name in img_list:
    path = "C:\\Users\\Code-Warriorr\\Desktop\\Code2024\\Computer Vision\\Img"
    plus = path + "\\" + name
    
    content = cv.imread(plus)
    content = cv.resize(content,(1000,700))
    
    addr = content
    
    txt = cv.putText(
        addr,
        text = "Album of Abhishek",
        org = (50,600),
        fontFace = cv.FONT_HERSHEY_DUPLEX,
        fontScale = 3,
        color = (10,150,150),
        thickness = 2,
        lineType = cv.LINE_4,
        bottomLeftOrigin = False,
    )
    
    cv.imshow("Winsows of Abhi",content)
    
    cv.waitKey(5000)
    
cv.destroyAllWindows()