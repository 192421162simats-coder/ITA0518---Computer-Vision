import cv2
import numpy as np

# Read the input image
img = cv2.imread("image1.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Unable to load image.")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Define source points
    src_points = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    # Define destination points
    dst_points = np.float32([
        [50, 50],
        [cols - 100, 50],
        [0, rows - 50],
        [cols - 50, rows - 100]
    ])

    # Calculate Homography matrix using DLT
    H, _ = cv2.findHomography(src_points, dst_points, method=0)

    # Apply the transformation
    transformed_img = cv2.warpPerspective(
        img,
        H,
        (cols, rows)
    )

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the transformed image
    cv2.imshow("DLT Transformation", transformed_img)

    # Save the transformed image
    cv2.imwrite(
        "transformation_using_DLT_Image.jpg",
        transformed_img
    )

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    print("DLT transformation completed successfully.")