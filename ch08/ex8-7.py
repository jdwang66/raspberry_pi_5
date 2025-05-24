import cv2
import numpy as np
import sys

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

rows,cols=img.shape[:2]

# 影像的左上角, 右上角, 左下角
src=np.float32([[0,0],[cols-1,0],[0,rows-1]])

# 影像的左上角, 上60%的點, 下40%的點
des=np.float32([[0,0],[int(0.6*(cols-1)),0],[int(0.4*(cols-1)),rows-1]])

matrix=cv2.getAffineTransform(src,des)  # 取得仿射轉換矩陣
img2=cv2.warpAffine(img,matrix,(cols,rows))  # 仿射轉換運算

cv2.imshow('Affine',img2)  # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()
