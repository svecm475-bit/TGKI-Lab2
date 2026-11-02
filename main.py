import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Камера не найдена")
    exit()

print("S to save")
print("Q to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        cv2.imwrite("foto.png", frame)
        print("gespeichert!")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
