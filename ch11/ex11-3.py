import sys
import time
import cv2
import mediapipe as mp
import numpy as np
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

# 參數
COUNTER, FPS = 0, 0
START_TIME = time.time()
DETECTION_RESULT = None

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# save_result
def save_result(result: mp.tasks.vision.GestureRecognizerResult, 
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
model = 'models/gesture_recognizer.task'

# 配置參數  
options = mp.tasks.vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model),
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,    
    result_callback=save_result)
  
# 建立物件偵測任務
detector = mp.tasks.vision.GestureRecognizer.create_from_options(options)

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

    # 執行手勢偵測
    detector.recognize_async(mp_image, time.time_ns() // 1_000_000)

    img2=np.copy(image)

    # 顯示FPS
    fps_text=f"FPS={FPS:0.1f}"
    cv2.putText(img2, fps_text, (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)
    
    # 顯示偵測結果
    if DETECTION_RESULT:
        gestures_list=DETECTION_RESULT.gestures
        hand_landmarks_list = DETECTION_RESULT.hand_landmarks
        handedness_list = DETECTION_RESULT.handedness

        if (len(gestures_list) > 0):
            gesture=gestures_list[0][0].category_name
        else:
            gesture=""            
        
        # Loop through the detected hands to visualize.
        for idx in range(len(hand_landmarks_list)):
            
            hand_landmarks = hand_landmarks_list[idx]
            handedness = handedness_list[idx]

            # Draw the hand landmarks.
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
            ])
            solutions.drawing_utils.draw_landmarks(
                img2,
                hand_landmarks_proto,
                solutions.hands.HAND_CONNECTIONS,
                solutions.drawing_styles.get_default_hand_landmarks_style(),
                solutions.drawing_styles.get_default_hand_connections_style())

            # Get the top left corner of the detected hand's bounding box.
            height, width, _ = img2.shape
            x_coordinates = [landmark.x for landmark in hand_landmarks]
            y_coordinates = [landmark.y for landmark in hand_landmarks]
            text_x = int(min(x_coordinates) * width)
            text_y = int(min(y_coordinates) * height) - 10

            # Draw handedness (left or right hand) on the image.
            cv2.putText(img2, f"{handedness[0].category_name, gesture}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                1, (0,255,255), 1, cv2.LINE_AA)

        cv2.imshow('gesture_recognizer', img2)

        if cv2.waitKey(1) == 27:
            break


detector.close()
cap.release()
cv2.destroyAllWindows()
