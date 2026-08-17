import cv2
import os

image_path = r"C:\Users\Admin\OneDrive\Desktop\ITA0518\Lab\EXP-16\Image1.png"

print("Image exists:", os.path.exists(image_path))

img = cv2.imread(image_path, 0)

if img is None:
    print("ERROR: Cannot read image1.jpg")
else:
    edges = cv2.Canny(img, 100, 200)

    output_path = r"C:\Users\Admin\OneDrive\Desktop\ITA0518\Lab\EXP-16\Edges.jpg"
    cv2.imwrite(output_path, edges)

    print("Edge detection completed successfully!")
    print("Output saved at:", output_path)
