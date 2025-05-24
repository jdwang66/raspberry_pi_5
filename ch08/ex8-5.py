import cv2
import numpy as np
import sys

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

num_rows, num_cols = img.shape[:2]  # 取得影像的列數, 行數

# 先進行平移, 向右移影像行數的一半, 向下移影像列數的一半
matrix=np.float32([[1,0,int(num_cols*0.5)],[0,1,int(num_rows*0.5)]])

# 平移運算, 結果影像的大小為原影像的2倍
img2=cv2.warpAffine(img,matrix,(num_cols*2,num_rows*2))  

# 旋轉的轉換矩陣, 平移運算後, 旋轉中心為原本影像的(行數,列數)
matrix=cv2.getRotationMatrix2D((num_cols, num_rows),60,1)

# 旋轉運算, 結果影像的大小為原影像的2倍, 避免截圖現象
img3=cv2.warpAffine(img2, matrix, (num_cols*2, num_rows*2))

cv2.imshow('Rotation', img3)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()
