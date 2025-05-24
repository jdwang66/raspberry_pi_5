import cv2
import sys
import matplotlib.pyplot as plt

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

# 轉為 rgb
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 轉為灰階
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, img_thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# 顯示影像
plt.subplot(121)
plt.imshow(img_rgb)
plt.title('original image')

plt.subplot(122)
plt.imshow(img_thresh, cmap='gray')
plt.title('binary image')

plt.show()
