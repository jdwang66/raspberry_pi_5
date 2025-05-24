import cv2
import numpy as np
import mediapipe as mp
from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
import matplotlib.pyplot as plt

# 設定影像及模型路徑
image_file='images/girl01.jpg'
model_path='models/face_landmarker.task'

# 載入影像
mp_image=mp.Image.create_from_file(image_file)

# 將影像轉為 numpy 陣列
img=np.copy(mp_image.numpy_view())
img2=np.copy(img)

# 配置選項
options=mp.tasks.vision.FaceLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),    
    running_mode=mp.tasks.vision.RunningMode.IMAGE
)

# 建立人臉標記偵測任務
with mp.tasks.vision.FaceLandmarker.create_from_options(options) as detector:
    # 執行人臉標記
    detection_result=detector.detect(mp_image)

    # 儲存執行結果
    face_landmarks_list=detection_result.face_landmarks
    
    for id in range(len(face_landmarks_list)):
        # 依序取出偵測到的人臉
        face_landmarks=face_landmarks_list[id]        

        # 取出 478 點標記
        face_landmarks_proto=landmark_pb2.NormalizedLandmarkList()
        for landmark in face_landmarks:
            face_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x,y=landmark.y, z=landmark.z)
            ])

        # 畫人臉網格
        solutions.drawing_utils.draw_landmarks(
            image=img2,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style(),
        )
        
        solutions.drawing_utils.draw_landmarks(
            image=img2,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style(),
        )

        solutions.drawing_utils.draw_landmarks(
            image=img2,
            landmark_list=face_landmarks_proto,
            connections=mp.solutions.face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_iris_connections_style(),
        )

# 顯示影像
plt.subplot(121)
plt.imshow(img)
plt.title('original image')

plt.subplot(122)
plt.imshow(img2)
plt.title('face landmark detection image')

plt.show()

    
