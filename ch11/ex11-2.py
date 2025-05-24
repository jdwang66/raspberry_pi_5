import sys
import time
import cv2
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import numpy as np

# 參數
COUNTER, FPS = 0, 0
START_TIME = time.time()
DETECTION_RESULT = None

# save_result
def save_result(result: mp.tasks.vision.HandLandmarkerResult, 
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
model = 'models/hand_landmarker.task'

# 配置參數
base_options = mp.tasks.BaseOptions(model_asset_path=model)
options = mp.tasks.vision.HandLandmarkerOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    num_hands=1,
    result_callback=save_result)

# 建立任務
detector = mp.tasks.vision.HandLandmarker.create_from_options(options)

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

    # 執行手部標記偵測
    detector.detect_async(mp_image, time.time_ns() // 1_000_000)

    img2=np.copy(image)   

    # 顯示FPS
    fps_text=f"FPS={FPS:0.1f}"
    cv2.putText(img2, fps_text, (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)

    # 顯示偵測結果
    if DETECTION_RESULT:
        hand_landmarks_list = DETECTION_RESULT.hand_landmarks
        handedness_list = DETECTION_RESULT.handedness

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
            cv2.putText(img2, f"{handedness[0].category_name}",
                (text_x, text_y), cv2.FONT_HERSHEY_DUPLEX,
                1, (0,255,255), 1, cv2.LINE_AA)
        
        cv2.imshow('hand_landmark_detection', img2)

        if cv2.waitKey(1) == 27:
            break


detector.close()
cap.release()
cv2.destroyAllWindows()



