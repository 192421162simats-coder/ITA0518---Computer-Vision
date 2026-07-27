import cv2

# Open webcam (Windows DirectShow)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

print("Webcam started successfully.")
print("Press:")
print("  S - Slow Motion")
print("  N - Normal Motion")
print("  F - Fast Motion")
print("  Q - Quit")

# Default speed
delay = 30

while True:
    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow("Webcam Video", frame)

    # Wait according to selected speed
    key = cv2.waitKey(delay) & 0xFF

    if key == ord('s'):
        delay = 100
        print("Slow Motion")

    elif key == ord('n'):
        delay = 30
        print("Normal Motion")

    elif key == ord('f'):
        delay = 10
        print("Fast Motion")

    elif key == ord('q'):
        print("Exiting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
