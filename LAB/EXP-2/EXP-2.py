import cv2

# Read the image
image = cv2.imread("image.jpg")   # Replace with your image file path

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blurred Image", blurred_image)

    # Save the blurred image (optional)
    cv2.imwrite("blurred_image.jpg", blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
