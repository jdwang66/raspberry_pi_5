import cv2
import sys
import matplotlib.pyplot as plt

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

# 轉為 rgb
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 加強影像
img2 = cv2.convertScaleAbs(img, alpha=1.2, beta=10)
img_bright = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# 強化細節
img3=cv2.detailEnhance(img)
img_enhance=cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)


# 顯示影像
plt.subplot(221)
plt.imshow(img_rgb)
plt.title('original image')

plt.subplot(222)
plt.imshow(img_bright)
plt.title('bright image')

plt.subplot(223)
plt.imshow(img_enhance)
plt.title('enhance image')

plt.show()
