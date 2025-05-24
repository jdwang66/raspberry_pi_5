import cv2
import sys

# 讀取影像, 轉為灰階
img = cv2.imread('images/girl01.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Image not found")
    sys.exit(1)

# 顯示影像
cv2.imshow('Gray Image', img)

# 儲存影像
cv2.imwrite('images/gray_img.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


