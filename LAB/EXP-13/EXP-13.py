
import cv2
import numpy as np

# Open the default webcam
camera = cv2.VideoCapture(0)

# Define source points in the original frame
source_points = np.float32([
    [150, 200],
    [450, 200],
    [550, 500],
    [50, 500]
])

# Define destination points
destination_points = np.float32([
    [0, 0],
    [400, 0],
    [400, 600],
    [0, 600]
])

# Compute the perspective transformation matrix
perspective_matrix = cv2.getPerspectiveTransform(
    source_points,
    destination_points
)

# Start capturing video
while camera.isOpened():

    success, frame = camera.read()

    if not success:
        print("Unable to capture video.")
        break

    # Apply perspective transformation
    transformed_frame = cv2.warpPerspective(
        frame,
        perspective_matrix,
        (400, 600)
    )

    # Display the original video
    cv2.imshow("Live Video", frame)

    # Display the perspective-transformed video
    cv2.imshow("Perspective View", transformed_frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
camera.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

