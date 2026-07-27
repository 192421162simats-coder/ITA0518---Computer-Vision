import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

# Create a kernel (3x3 matrix)
kernel = np.ones((3, 3), np.uint8)

# Apply erosion
eroded_img = cv2.erode(img, kernel, iterations=1)

# Display the original and eroded images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded_img)

# Save the eroded image
cv2.imwrite("eroded_image.jpg", eroded_img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
