import cv2
import sys

# 開啟 webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    sys.exit(1)

while cap.isOpened():
    # 取得影像
    ret, frame = cap.read()  
    if not ret:
        break

	# 調整影像大小
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # 轉為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Canny 邊緣運算
    edge = cv2.Canny(gray, 50, 150)

    # 顯示影像
    cv2.imshow('Frame', edge)

    # 按 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
