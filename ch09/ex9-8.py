import cv2
import sys

roi_start=(0,0)
roi_end=(0,0)
dragging=False

# 滑鼠事件處理函式
def draw_rectangle(event,x,y,flags,param):
    global roi_start, roi_end, dragging

    if event==cv2.EVENT_LBUTTONDOWN:
        dragging=True
        roi_start=(x,y)
    elif event==cv2.EVENT_MOUSEMOVE:
        if dragging:
            roi_end=(x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        dragging=False
        roi_end=(x,y)

# 開啟 webcam
cap=cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open webcam")
    sys.exit(1)

# 指定視窗名稱
main_window="Webcam"
cv2.namedWindow(main_window)

# 偵測指定視窗下的滑鼠事件
cv2.setMouseCallback(main_window, draw_rectangle)

while True:
    # 取得影像
    ret, frame = cap.read()
    if not ret:
        break

    # 在影像中畫矩形 roi
    cv2.rectangle(frame, roi_start, roi_end, (0,0,255),2)

    # 顯示 roi
    if roi_end[1] > roi_start[1] and roi_end[0] > roi_start[0]:
        roi = frame[roi_start[1]:roi_end[1], roi_start[0]:roi_end[0]]
        cv2.imshow("ROI",roi)
    
    # 顯示影像
    cv2.imshow(main_window, frame)

    # 按 q 鍵離開
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

