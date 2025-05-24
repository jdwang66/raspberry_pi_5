import cv2
import numpy as np
import sys

img=cv2.imread('images/girl01.jpg')
if img is None:
    print("Image not found")
    sys.exit(1)

num_rows, num_cols = img.shape[:2]  # 取得影像的列數, 行數

matrix = np.float32([[1,0,70],[0,1,110]])  # 平移轉換矩陣

# 執行轉換
img2=cv2.warpAffine(img, matrix, (num_cols+140, num_rows+220))

cv2.imshow('Translation', img2)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()
