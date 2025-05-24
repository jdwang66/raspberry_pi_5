import mediapipe as mp
import numpy as np
from mediapipe.framework.formats import landmark_pb2
from mediapipe import solutions
import matplotlib.pyplot as plt

# 設定影像及模型路徑
image_file='images/sport01.jpg'
model_path = 'models/pose_landmarker_full.task'

# 載入影像
mp_image=mp.Image.create_from_file(image_file)

# 將影像轉為 numpy 陣列
img=np.copy(mp_image.numpy_view())
img2=np.copy(img)

# 配置參數
options = mp.tasks.vision.PoseLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),    
    running_mode=mp.tasks.vision.RunningMode.IMAGE)

# 建立姿勢標記偵測任務
with mp.tasks.vision.PoseLandmarker.create_from_options(options) as landmarker:
    # 執行姿勢標記偵測
    pose_landmarker_result = landmarker.detect(mp_image)

    # 儲存偵測結果
    pose_landmarks_list = pose_landmarker_result.pose_landmarks
    
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
            
            # 印出33點標記座標及存在分數
            print(f"[{idx}, {id}, {x:.2f}, {y:.2f}, {z:.2f}, {v:.2f}]")
            extend_list.append(landmark_pb2.NormalizedLandmark(x=x,y=y,z=z))
        
        # 畫姿勢標記
        pose_landmarks_proto.landmark.extend(extend_list)
        option=solutions.drawing_utils.DrawingSpec(color=(255,0,0), thickness=3)
        solutions.drawing_utils.draw_landmarks(
            img2,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,            
            solutions.drawing_styles.get_default_pose_landmarks_style(),
        )

# 顯示影像
plt.subplot(121)
plt.imshow(img)
plt.title('original image')

plt.subplot(122)
plt.imshow(img2)
plt.title('pose landmark detection image')

plt.show()



