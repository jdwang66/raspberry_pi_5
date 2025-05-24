# 侵蝕及膨脹
import cv2
import sys
import matplotlib.pyplot as plt

# 讀取影像
img=cv2.imread('images/fruit01.jpg')  
if img is None:
    print("Image not found")
    sys.exit(1)

# 影像轉為 RGB 及 GRAY
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# GRAY 影像反相
img2=cv2.bitwise_not(img_gray)

# 影像二值化
ret, img_thresh=cv2.threshold(img2, 0, 255, cv2.THRESH_OTSU)

# 取得結構元素的形狀
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))

# 先膨脹, 再侵蝕, 消除黑色小點
img_dilation=cv2.dilate(img_thresh, kernel) 
img_erosion=cv2.erode(img_dilation, kernel) 

# 顯示影像
plt.subplot(221)
plt.imshow(img_rgb)
plt.title('original image')

plt.subplot(222)
plt.imshow(img_thresh, cmap='gray')
plt.title('binary image')

plt.subplot(223)
plt.imshow(img_dilation, cmap='gray')
plt.title('dilation image')

plt.subplot(224)
plt.imshow(img_erosion, cmap='gray')
plt.title('erosion image')

plt.show()
