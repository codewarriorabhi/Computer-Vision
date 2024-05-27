import cv2 as cv


img = cv.imread(r"C:\Users\Code-Warriorr\Desktop\Code2024\Computer Vision\Img\spider-man.png")
img = cv.resize(img,(600,500))

img2 = img

txt_on_img = cv.putText(
    img2,
    text = "SpiderMan",
    org = (100,400),
    fontFace = cv.FONT_HERSHEY_DUPLEX,
    fontScale = 3,
    color = (0,150,150),
    thickness = 3,
    lineType = cv.LINE_8,
    bottomLeftOrigin = False
)

cv.imshow("Warriorr",img)

cv.waitKey(0)
cv.destroyAllWindows()