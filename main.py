import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
    exit()

print("S to save")
print("Q to exit")
counter = 11
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        cv2.imwrite(f"foto{counter}.png", frame)
        print("saved")
        counter += 1

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
