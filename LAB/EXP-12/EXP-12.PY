import cv2
import numpy as np

# Read the input image
image = cv2.imread("image1.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Get image dimensions
    rows, cols = image.shape[:2]

    # Define source points
    source_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Define destination points
    destination_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [int(0.33 * cols), rows - 1],
        [int(0.66 * cols), rows - 1]
    ])

    # Compute the perspective transformation matrix
    transform_matrix = cv2.getPerspectiveTransform(
        source_points,
        destination_points
    )

    # Apply the perspective transformation
    transformed_image = cv2.warpPerspective(
        image,
        transform_matrix,
        (cols, rows)
    )

    # Save the transformed image
    cv2.imwrite("Perspective_Transformed_Image.jpg", transformed_image)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformed Image", transformed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()