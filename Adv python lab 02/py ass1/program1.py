import cv2

# Load image directly
image = cv2.imread("river.jpg")

if image is None:
    print("Image not found! Make sure river.jpg is in the same folder.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Detection", edges)

    print("Edge detection completed successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()