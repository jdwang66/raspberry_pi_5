import cv2
import sys

# 開啟webcam
cap = cv2.VideoCapture(1)  
if not cap.isOpened():
	print("Cannot open webcam")
	sys.exit(1)

while True:
	# 取得影像
	ret, frame = cap.read()  
	if not ret:
		print("read error")
		break

	# 顯示影像
	cv2.imshow('Image', frame)

	# 按q鍵離開
	if cv2.waitKey(1) & 0xFF == ord('q'):  
		break

cap.release()
cv2.destroyAllWindows()

