import cv2
import numpy as np
import sys

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

rows,cols=img.shape[:2]

# 選取投影轉換的4個點
src=np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
des=np.float32([[0,0],[cols-1,0],[int(0.4*(cols-1)),rows-1],[int(0.6*cols-1),rows-1]])

# 取得投影轉換的轉換矩陣
matrix=cv2.getPerspectiveTransform(src,des)

# 執行投影轉換
img2=cv2.warpPerspective(img,matrix,(cols,rows))

cv2.imshow('Affine',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
