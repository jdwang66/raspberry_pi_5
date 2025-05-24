import cv2
import sys

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

# 放大1.2倍, 內插方式不同
img2=cv2.resize(img, None, fx=1.2,fy=1.2, interpolation=cv2.INTER_LINEAR)
img3=cv2.resize(img, None, fx=1.2,fy=1.2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Scaling-Linear', img2)
cv2.imshow('Scaling-Cubic', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
