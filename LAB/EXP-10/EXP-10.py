
import cv2

# Load the image
image = cv2.imread("image1.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Display the image
    cv2.imshow("Original Image", image)

    # Move the window to position (300, 200)
    cv2.moveWindow("Original Image", 300, 200)

    # Wait until any key is pressed
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()

