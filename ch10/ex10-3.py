import cv2
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

# 設定影像及模型路徑
image_file='images/girl01.jpg'
model_path='models/blaze_face_short_range.tflite'

# 載入影像
mp_image=mp.Image.create_from_file(image_file)

# 將影像轉為 numpy 陣列
img=np.copy(mp_image.numpy_view())
img2=np.copy(img)

# 取出影像形狀
h,w,c=img2.shape

# 配置選項
options=mp.tasks.vision.FaceDetectorOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    running_mode=mp.tasks.vision.RunningMode.IMAGE
)

# 建立人臉偵測任務
with mp.tasks.vision.FaceDetector.create_from_options(options) as detector:
    # 執行人臉偵測
    detection_result=detector.detect(mp_image)

    for detection in detection_result.detections:
        # 畫邊界框
        bbox=detection.bounding_box
        x1=bbox.origin_x
        y1=bbox.origin_y
        width=bbox.width
        height=bbox.height
        cv2.rectangle(img2, (x1,y1), (x1+width, y1+height), (0,0,255), 3)

        # 畫人臉特徵
        for keypoint in detection.keypoints:
            cx=int(keypoint.x*w)
            cy=int(keypoint.y*h)
            cv2.circle(img2,(cx,cy),5,(255,0,0),-1)

# 顯示影像
plt.subplot(121)
plt.imshow(img)
plt.title('original image')

plt.subplot(122)
plt.imshow(img2)
plt.title('face detection image')

plt.show()


    
