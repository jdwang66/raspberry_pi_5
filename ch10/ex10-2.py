import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt

# 影像及模型路徑
image_file='images/girl06.jpg'
model_path = 'models/selfie_segmenter.tflite'

# 載入影像
mp_image=mp.Image.create_from_file(image_file)

# 將影像轉為 numpy 陣列
img=np.copy(mp_image.numpy_view())

# 建置參數
options = mp.tasks.vision.ImageSegmenterOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    running_mode=mp.tasks.vision.RunningMode.IMAGE,
    output_category_mask=True)

# 建立影像分割任務
with mp.tasks.vision.ImageSegmenter.create_from_options(options) as segmenter:
    # 執行影像分割
    segmentation_result = segmenter.segment(mp_image)    

    # 取得影像分割遮罩
    category_mask = segmentation_result.category_mask
    
    # 建立背景影像    
    bg_image = np.zeros(img.shape, dtype=np.uint8)
    bg_image[:] = (192,192,192)  # gray

    # 根據 category_mask 的值，生成一個新的 output_image
    # 若 category_mask > 0.2, 顯示 bg_image, 否則顯示 img
    condition = np.stack((category_mask.numpy_view(),) * 3, axis=-1) > 0.2
    img2 = np.where(condition, bg_image, img)

# 顯示影像
plt.subplot(121)
plt.imshow(img)
plt.title('original image')

plt.subplot(122)
plt.imshow(img2)
plt.title('image segmentation image')

plt.show()




