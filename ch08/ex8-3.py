import cv2
import sys

img = cv2.imread('images/girl01.jpg')

if img is None:
    print("Image not found")
    sys.exit(1)

# 轉為HSV
hsv_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

cv2.imshow('H channel', hsv_img[:, :, 0])  # 顯示H通道
cv2.imshow('S channel', hsv_img[:, :, 1])  # 顯示S通道
cv2.imshow('V channel', hsv_img[:, :, 2])  # 顯示V通道

cv2.waitKey(0)
cv2.destroyAllWindows()


