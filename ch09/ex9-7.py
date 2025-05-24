import cv2
import matplotlib.pyplot as plt
import sys

# 讀取影像
image_file='images/girl01.jpg'
img=cv2.imread(image_file)
if img is None:
    print("Image not found")
    sys.exit(1)

# img 轉 RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 定義 roi
img_roi=img[30:150, 120:270] # y1:y2, x1:x2

# 複製原始影像 
img_with_roi = img.copy()

# 畫矩形 roi
cv2.rectangle(img_with_roi, (120, 30), (270, 150), (0, 0, 255), 2)

# 顯示影像
plt.subplot(121)
plt.imshow(img_with_roi)
plt.title('image with roi')

plt.subplot(122)
plt.imshow(img_roi)
plt.title('roi')

plt.show()
