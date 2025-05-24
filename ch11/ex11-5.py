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
def save_result(result: mp.tasks.vision.PoseLandmarkerResult, 
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
model = 'models/pose_landmarker_full.task'

# 配置參數
base_options = mp.tasks.BaseOptions(model_asset_path=model)
options = mp.tasks.vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,    
    result_callback=save_result)

# 建立任務
detector = mp.tasks.vision.PoseLandmarker.create_from_options(options)

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

    # 執行姿勢標記偵測
    detector.detect_async(mp_image, time.time_ns() // 1_000_000)

    img2=np.copy(image)   

    # 顯示FPS
    fps_text=f"FPS={FPS:0.1f}"
    cv2.putText(img2, fps_text, (24, 50), cv2.FONT_HERSHEY_DUPLEX,
                1, (255,255,0), 1, cv2.LINE_AA)

    # 顯示偵測結果
    if DETECTION_RESULT:
        # 儲存偵測結果
        pose_landmarks_list = DETECTION_RESULT.pose_landmarks
        
        for idx in range(len(pose_landmarks_list)):
            # 依序取出每個人體姿勢
            pose_landmarks = pose_landmarks_list[idx]

            # 取出標記
            pose_landmarks_proto=landmark_pb2.NormalizedLandmarkList()

            extend_list=[]
            for id, landmark in enumerate(pose_landmarks):
                # 依序取出33點標記座標, 及存在分數
                x=landmark.x
                y=landmark.y
                z=landmark.z
                v=landmark.visibility
                
                # 印出33點標記座標
                print(f"[{idx}, {id}, {x:.2f}, {y:.2f}, {z:.2f}, {v:.2f}]")
                extend_list.append(landmark_pb2.NormalizedLandmark(x=x,y=y,z=z))
            
            # 畫姿勢標記
            pose_landmarks_proto.landmark.extend(extend_list)
            option=solutions.drawing_utils.DrawingSpec(color=(255,0,0), thickness=3)
            solutions.drawing_utils.draw_landmarks(
                img2,
                pose_landmarks_proto,
                solutions.pose.POSE_CONNECTIONS,
                # option
                solutions.drawing_styles.get_default_pose_landmarks_style(),
            )
        
        cv2.imshow('face_detection', img2)

        if cv2.waitKey(1) == 27:
            break


detector.close()
cap.release()
cv2.destroyAllWindows()



