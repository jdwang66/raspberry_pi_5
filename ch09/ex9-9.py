import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import time

# 開啟 webcam
cap=cv2.VideoCapture(1)
if not cap.isOpened():
    print("Failed to open camera.")
    sys.exit(1)

# 建立 BackgroundSubtractorMOG2 物件
bg_sub=cv2.createBackgroundSubtractorMOG2(
history=100, varThreshold=50, detectShadows=True)

# 定義平均值串列變數
mean_list=[]

# 取得figure及ax物件
fig, ax = plt.subplots()

# 開啟互動模式
plt.ion()

# 取得 frame, 轉為灰階
ret, frame = cap.read()
gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 選擇 roi
roi=cv2.selectROI(frame)

# 在gray_img, 取出 roi
x1=int(roi[0])
x2=x1+int(roi[2])
y1=int(roi[1])
y2=y1+int(roi[3])
roi1 = gray_img[y1:y2, x1:x2]

# 取得去除背景結果    
fg_mask=bg_sub.apply(roi1)

# 計算 mask 平均值, 將其加入 mean_list 串列中
mean_value = np.mean(fg_mask)    
mean_list.append(mean_value)

cv2.destroyAllWindows()

# 圖形最多顯示200點資料
num = 200

while True:
    # 取得 frame
    ret, frame = cap.read()
    if not ret:
        break
    
    # frame 轉為灰階
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 在gray_img, 取出 roi
    # roi : (x, y, w, h)    
    roi2 = gray_img[y1:y2, x1:x2]

    # 在 frame 繪矩形 ROI
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # 取得 roi 去除背景結果    
    fg_mask=bg_sub.apply(roi2)    

    # 計算 mask 平均值, 將其加入 mean_list 串列中
    mean_value = np.mean(fg_mask)    
    mean_list.append(mean_value)

    # 判斷是否有物件運動
    if mean_value > 5:
        print(f"mean_value: {mean_value}, 有物件運動")

    # 更新圖形
    ax.clear()
    ax.plot(mean_list)

    # 若資料超過 200 點, 更新 x 軸顯示範圍 
    disp_num=len(mean_list)
    if disp_num > num:
        ax.set_xlim(disp_num-num, disp_num)
    
    plt.pause(0.01)

    # 顯示影像
    cv2.imshow('Frame', frame)

    # 按 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 關閉互動模式
plt.ioff()

# 保持視窗開啟
plt.show()

