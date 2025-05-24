import cv2
import sys

img = cv2.imread('images/girl01.jpg')
print(img.shape)
print(img.size)
print(img.dtype)


if img is None:
    print("Image not found")
    sys.exit(1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
