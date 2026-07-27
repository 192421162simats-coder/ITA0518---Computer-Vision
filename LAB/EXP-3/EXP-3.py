import cv2

# Read the image
image = cv2.imread("sample.jpg")

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display the original and edge-detected images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
