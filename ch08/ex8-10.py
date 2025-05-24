import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, std=25):
    noise = (np.random.normal(mean, std, image.shape)*0.02).astype(np.uint8)    
    noisy_image = cv2.add(image, noise)
    return noisy_image

img=cv2.imread('images/girl01.jpg')  # 取得影像
if img is None:
    print("Image not found")
    sys.exit(1)

# 轉為 rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 取得影像的列數及行數
row, col, ch = img.shape

# 加入雜訊
noisy = add_gaussian_noise(img)

# blur
img_blur = cv2.blur(noisy, (5,5))

# Gaussian
img_gaussian = cv2.GaussianBlur(noisy, (5, 5),0)

# Median
img_median = cv2.medianBlur(noisy, 5)



# 顯示影像
plt.subplot(221)
plt.imshow(noisy)
plt.title('original image')

plt.subplot(222)
plt.imshow(img_blur, cmap='gray')
plt.title('blur image')

plt.subplot(223)
plt.imshow(img_gaussian)
plt.title('GaussBlur image')

plt.subplot(224)
plt.imshow(img_median)
plt.title('mediaBlur image')

plt.show()