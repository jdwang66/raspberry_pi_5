import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np

# 設定影像及模型路徑
image_file='images/dog03.jpg'
model_path='models/efficientdet_lite0.tflite'

# 載入影像
mp_image=mp.Image.create_from_file(image_file)

# 將影像轉為 numpy 陣列
img=np.copy(mp_image.numpy_view())
h,w,c=img.shape
img2=np.copy(img)

# 配置參數
options = mp.tasks.vision.ObjectDetectorOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    score_threshold=0.5,
    max_results=2,
    running_mode=mp.tasks.vision.RunningMode.IMAGE)


# 建立物件偵測任務
with mp.tasks.vision.ObjectDetector.create_from_options(options) as detector:
    # 執行物件偵測    
    detection_result = detector.detect(mp_image)    

    for detection in detection_result.detections:
        # 畫邊界框
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        cv2.rectangle(img2, start_point, end_point, (0,0,255), 2)

        # 顯示標籤及分數
        category = detection.categories[0]
        category_name = category.category_name
        probability = round(category.score, 2)
        result_text = category_name + ' (' + str(probability) + ')'        
        text_location = (bbox.origin_x, bbox.origin_y-30)
        cv2.putText(img2, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                    2, (255,0,0), 3)    

# 顯示影像
plt.subplot(121)
plt.imshow(img)
plt.title('original image')

plt.subplot(122)
plt.imshow(img2)
plt.title('object detection image')

plt.show()

