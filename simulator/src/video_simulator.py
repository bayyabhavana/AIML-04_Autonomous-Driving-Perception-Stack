
import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Checking webcam...")

if not camera.isOpened():
    print("Webcam not available!")
    exit()

print("Webcam connected!")

frame_count = 0

while True:
    success, frame = camera.read()

    if not success:
        print("Failed to capture frame!")
        break

    frame_count += 1

    cv2.putText(
        frame,
        "LIVE CAMERA TEST",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print("Frames captured:", frame_count)
print("Webcam test completed!")
