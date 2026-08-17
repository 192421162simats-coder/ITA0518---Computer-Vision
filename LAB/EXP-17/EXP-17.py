import cv2
import numpy as np

img = cv2.imread("image1.png", 0)

sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

cv2.imwrite("sobel_x.jpg", sobel_x)

print("Sobel X edge detection completed successfully!")