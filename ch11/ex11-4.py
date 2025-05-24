import sys
import time
import cv2
import mediapipe as mp

# 參數
COUNTER, FPS = 0, 0
START_TIME = time.time()
DETECTION_RESULT = None

# save_result
def save_result(result: mp.tasks.vision.FaceDetectorResult, 
                unused_output_image: mp.Image,
                timestamp_ms: int):
    
        global FPS, COUNTER, START_TIME, DETECTION_RESULT

        # Calculate the FPS
        if COUNTER % 10 == 0:
            FPS = 10 / (time.time() - START_TIME)
            START_TIME = time.time()

        DETECTION_RESULT = result
        COUNTER += 1        

# 模型
model = 'models/blaze_face_short_range.tflite'

# 配置參數
base_options = mp.tasks.BaseOptions(model_asset_path=model)
options = mp.tasks.vision.FaceDetectorOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    min_detection_confidence=0.5,
    min_suppression_threshold=0.5,
    result_callback=save_result)

# 建立任務
detector = mp.tasks.vision.FaceDetector.create_from_options(options)

# webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while cap.isOpened():
    # 讀取影像
    success, image = cap.read()
    if not success:
        sys.exit('read webcam error.')

    # 轉為 mp image
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

    # 執行人臉偵測
    detector.detect_async(mp_image, time.time_ns() // 1_000_000)

    img2=image

    # 顯示FPS
    fps_text=f"FPS={FPS:0.1f}"
    cv2.putText(img2, fps_text, (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)

    # 顯示偵測結果
    if DETECTION_RESULT:
        for detection in DETECTION_RESULT.detections:
            # 畫邊界框
            bbox = detection.bounding_box
            start_point = bbox.origin_x, bbox.origin_y
            end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height            
            cv2.rectangle(img2, start_point, end_point, (0, 165, 255), 3)

            # 顯示分數
            category = detection.categories[0]            
            probability = round(category.score, 2)
            result_text = str(probability)
            text_location = (bbox.origin_x + 10, bbox.origin_y + 40)
            cv2.putText(img2, result_text, text_location, cv2.FONT_HERSHEY_DUPLEX,
                1, (0,255,255), 1, cv2.LINE_AA)

        cv2.imshow('face_detection', img2)

        if cv2.waitKey(1) == 27:
            break


detector.close()
cap.release()
cv2.destroyAllWindows()



