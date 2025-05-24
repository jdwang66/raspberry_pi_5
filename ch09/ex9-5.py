import cv2
import sys

# 開啟 webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    sys.exit(1)

# 取得 frame1
ret, frame1 = cap.read()

while True:
    # 取得 frame2
    ret, frame2 = cap.read()
    if not ret:
        break

    # fram1 與 frame2 影像相減
    diff=cv2.absdiff(frame1, frame2)

    # 更新 frame1
    frame1=frame2

    # 顯示影像
    cv2.imshow('diff', diff)

    # 按 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
