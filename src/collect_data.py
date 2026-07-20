import cv2
import os

folder = "dataset/Hello"

os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)

count = len(os.listdir(folder))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.putText(
        frame,
        f"Images: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Collect Hello Images", frame)

    key = cv2.waitKey(1)

    if key == ord("c"):
        filename = os.path.join(folder, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        count += 1

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()