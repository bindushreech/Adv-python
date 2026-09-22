import cv2

# Open video
cap = cv2.VideoCapture("car.mp4")

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Display original and detected motion
    cv2.imshow("Original Video", frame)
    cv2.imshow("Motion Detection", fgmask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

