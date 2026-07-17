import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.putText(
        frame,
        "Crowd Detection Module",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Drone Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
