import cv2
import sys

# 開啟 wecam
cap=cv2.VideoCapture(0)
if not cap.isOpened():
	print("Cannot open webcam")
	sys.exit(1)

# 指定編碼格式
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

# 建立 VideoWriter物件, 指定欲寫入的視訊檔
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
	ret, frame = cap.read()

	if ret:
		# 將 frame 寫入視訊檔
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		print("read error.")
		break

cap.release()
out.release()
cv2.destroyAllWindows()
