import cv2 as cv


addr = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\Personal\CV_Photo_1.jpg")
addr = cv.resize(addr,(500,600))
img = addr

txt_img = cv.putText(
    img,
    text = "Abhishek Kumar",
    org = (100,550),
    color = (0,240,0),
    fontFace = cv.FONT_HERSHEY_DUPLEX,
    fontScale = 1,
    thickness = 5,
    lineType = 4,
    bottomLeftOrigin = False
)

img = txt_img

face_rectanguler = cv.rectangle(
    img,
    pt1 = (50,50),
    pt2 = (450,450),
    color = (0,255,0),
    lineType = 16,
    thickness = 5
)

cv.imshow("Warriorr",face_rectanguler)
cv.waitKey(0)
cv.destroyAllWindows()