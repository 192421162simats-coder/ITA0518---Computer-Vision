import cv2

# Read the input image
img = cv2.imread("image1.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Unable to load image.")
else:
    # Rotate 90 degrees clockwise
    clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Rotate 90 degrees counter-clockwise
    counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Save the rotated images
    cv2.imwrite("clockwise_image.jpg", clockwise)
    cv2.imwrite("counterclockwise_image.jpg", counterclockwise)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counterclockwise)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
