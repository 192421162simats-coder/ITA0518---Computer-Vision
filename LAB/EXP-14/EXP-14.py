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
        [0, 0],
        [cols - 1, 0],
        [0, int(0.7 * rows)],
        [cols - 1, int(0.7 * rows)]
    ])

    # Calculate the Homography matrix
    M, _ = cv2.findHomography(src_points, dst_points)

    # Apply Homography transformation
    homography_img = cv2.warpPerspective(
        img,
        M,
        (cols, rows)
    )

    # Save the transformed image
    cv2.imwrite(
        "transformation_using_Homography_Image.jpg",
        homography_img
    )

    # Display the original and transformed images
    cv2.imshow("Original Image", img)
    cv2.imshow("Homography Transformation", homography_img)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

    print("Homography transformation completed successfully.")
