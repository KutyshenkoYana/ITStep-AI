# Завдання 1
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть
# параметри
# Можете змінити розмір кадру для кращої візуалізації
# cv2.resize()

# import cv2
# import ultralytics
#
# model = ultralytics.YOLO("yolo11s.pt")
#
# cap = cv2.VideoCapture('meetings.mp4')
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         break
#
#     frame = cv2.resize(frame, None, fx=0.3, fy=0.3)
#
#     results = model.predict(
#         frame,
#         device="cpu",
#         conf=0.3,
#         iou=0.5
#     )
#
#     result = results[0]
#
#     cv2.imshow("orig", frame)
#     cv2.imshow("result", result.plot())
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


# Завдання 2
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та почніть показувати відео з
# моменту, коли людей стало 5

import cv2
import ultralytics

model = ultralytics.YOLO("yolo11s.pt")

cap = cv2.VideoCapture('meetings.mp4')

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, None, fx=0.3, fy=0.3)

    results = model.predict(
        frame,
        device="cpu",
        conf=0.3,
        iou=0.5
    )

    result = results[0]

    boxes = result.boxes

    people = 0

    for i in range(len(boxes)):
        box = boxes[i]

        cls = box.cls.cpu().numpy()
        class_id = int(cls[0])

        if class_id == 0:
            people += 1

    if people >= 5:
        cv2.imshow("result", result.plot())

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
