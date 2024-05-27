#Text Over a img



import cv2 as cv
 
 
img = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\astronaut-digital.jpg",1)
img = cv.resize(img,(600,500))
img2 = img

txt = cv.putText(img2,
text = "Warriorr",
org = (100,450),
fontFace = cv.FONT_HERSHEY_DUPLEX,
fontScale = 3,
color = (0,0,255),
thickness = 3,
lineType = cv.LINE_8,
bottomLeftOrigin = False)

cv.imshow("hello",img)

cv.waitKey(0)