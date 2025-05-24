# 邊緣偵測
import cv2
import sys

# 取得影像，轉為灰階
img=cv2.imread('images/fruit01.jpg')
if img is None:
    print("Image not found")
    sys.exit(1)

# 影像轉為 RGB 及 GRAY
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# sobel邊緣偵測
sobel_hor_img=cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_ver_img=cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# laplacian邊緣偵測
laplacian_img=cv2.Laplacian(img_gray, cv2.CV_64F)

# canny邊緣偵測
canny_img=cv2.Canny(img_gray, 50, 240)

# 顯示影像
cv2.imshow('Original', img)
cv2.imshow('Sobel hor', sobel_hor_img)
cv2.imshow('Laplacian', laplacian_img)
cv2.imshow('Canny', canny_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



