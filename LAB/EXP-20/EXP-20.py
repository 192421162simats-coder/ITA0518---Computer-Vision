import cv2
import numpy as np

img = cv2.imread("Image1.png")

kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imwrite("Sharpened_Image.jpg", sharpened)

print("Image sharpening completed successfully!")