import cv2
import sys

# 開啟 webcam
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open webcam")
    sys.exit(1)

# 建立 BackgroundSubtractorMOG2 物件
bg_subtractor=cv2.createBackgroundSubtractorMOG2(
history=100, varThreshold=50, detectShadows=True)

while cap.isOpened():
    # 取得 frame
    ret, frame = cap.read()
    if not ret:
        break

    # 取得去除背景結果    
    fg_mask=bg_subtractor.apply(frame)    

    # 顯示影像
    cv2.imshow('Mask', fg_mask)

    # 按 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
