import cv2

# Read the video file
cap = cv2.VideoCapture("video.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display the video
    cv2.imshow("Video Playback", frame)

    # Change the delay to control speed
    # Slow Motion: 100 ms delay
    # Normal Motion: 30 ms delay
    # Fast Motion: 10 ms delay

    key = cv2.waitKey(100) & 0xFF      # Slow Motion
    # key = cv2.waitKey(30) & 0xFF     # Normal Motion
    # key = cv2.waitKey(10) & 0xFF     # Fast Motion

    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
