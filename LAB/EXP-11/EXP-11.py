import cv2
import numpy as np

# Read the input image
image = cv2.imread("image1.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Get the image dimensions
    rows, cols = image.shape[:2]

    # Create the affine transformation matrix (Translation)
    transform_matrix = np.float32([
        [1, 0, 100],
        [0, 1, 50]
    ])

    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, transform_matrix, (cols, rows))

    # Save the transformed image
    cv2.imwrite("Affine_Transformed.jpg", transformed_image)

    # Display the images
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transformed Image", transformed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
