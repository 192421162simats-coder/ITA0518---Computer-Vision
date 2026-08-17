import cv2
import numpy as np

img = cv2.imread("Image1.png")

kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imwrite("Sharpened_Image.jpg", sharpened)

print("Image sharpening completed successfully!")