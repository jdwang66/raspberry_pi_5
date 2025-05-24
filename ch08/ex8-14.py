import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# 讀取影像
img = cv2.imread('images/fruit01.jpg')
if img is None:
    print("Image not found")
    sys.exit(1)

# 影像轉為 RGB 及灰階
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 灰階影像反相
img2=cv2.bitwise_not(img_gray)

# 影像二值化
ret, img_thresh = cv2.threshold(img2, 0, 255, cv2.THRESH_OTSU)

# 尋找 contours
contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 建立黑色畫布
img_contours = np.zeros(img.shape)

# 在黑色畫布, 繪製輪廓
cv2.drawContours(img_contours, contours, -1, (255,255,255), 3)

# 顯示影像
plt.subplot(221)
plt.imshow(img_rgb)
plt.title('original image')

plt.subplot(222)
plt.imshow(img_thresh, cmap='gray')
plt.title('binary image')

plt.subplot(223)
plt.imshow(img_contours)
plt.title('contour image')

plt.show()
