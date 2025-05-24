import cv2
import sys

# 開啟 webcam
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    sys.exit(1)

while cap.isOpened():
    ret,frame=cap.read()

    if ret:
        # frame 轉為灰階        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        h=gray.shape[0]  # frame 高
        w=gray.shape[1]  # frame 寬

        # 取出灰階影像的中心區域, 並進行高斯模糊處理
        gaussianblur = cv2.GaussianBlur(gray[h//4:3*h//4,w//4:3*w//4], (5, 5), 0)
        cv2.imshow('frame', frame)
        cv2.imshow('blur',gaussianblur)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
