import cv2
import numpy as np

img = cv2.imread("Image1.png", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.imwrite("Edge_detection.jpg", edges)

print("Sobel XY edge detection completed successfully!")
