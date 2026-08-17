import cv2
import numpy as np

img = cv2.imread("Image1.png", 0)

sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

cv2.imwrite("sobel_y.jpg", sobel_y)

print("Sobel Y edge detection completed successfully!")
