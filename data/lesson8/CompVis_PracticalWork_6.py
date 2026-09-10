# Завдання 1
# Отримайте перший кадр з файлу data\lesson8\animals.mp4
# та виведіть його на екран.
# Проведіть детекцію об’єктів зо допомогою YOLO та
# виведіть результати.
# Змініть параметри моделі conf та iou і подивіться як це
# впливає на результат.
# Отримайте рамки для кожного об’єкта, виріжіть їх та
# виведіть як окремі зображення

# import cv2
# import ultralytics
#
# model = ultralytics.YOLO("yolo11s.pt")
#
# cap = cv2.VideoCapture('animals.mp4')
#
# success, img = cap.read()
#
# img = cv2.resize(img, None, fx=0.5, fy=0.5)
#
# print(img.shape)
#
# cv2.imshow("orig", img)
#
# results = model.predict(
#     img,
#     device="cpu",
#     conf=0.25,
#     iou=0.5
# )
#
# print(results)
#
# result = results[0]
#
# names = result.names
# print(type(names))
# print(names)
#
# boxes = result.boxes
# print(boxes)
#
# cv2.imshow("result", result.plot())
#
# conf = boxes.conf
# print(type(conf))
#
# conf = conf.cpu()
# conf = conf.numpy()
#
# print(conf)
# print(conf.shape)
# print(conf.dtype)
#
# for i in range(len(boxes)):
#     box = boxes[i]
#
#     print(box)
#     print(box.conf)
#     print(box.cls)
#     print(box.xyxy)
#
#     conf = box.conf
#     conf = conf.cpu().numpy()
#
#     print(f"Ймовірність об'єкта {conf[0]}")
#
#     cls = box.cls
#     cls = cls.cpu().numpy()
#
#     print(f"Індекс класу об'єкта {cls[0]}")
#
#     class_id = int(cls[0])
#     class_name = names[class_id]
#
#     print(f"Клас об'єкта {class_name}")
#
#     xyxy = box.xyxy
#     print(xyxy)
#
#     xyxy = xyxy.cpu().numpy()
#     xyxy = xyxy.astype(int)
#
#     print(xyxy)
#
#     x1, y1, x2, y2 = xyxy[0]
#
#     roi = img[y1:y2, x1:x2]
#
#     cv2.imshow(f"roi {class_name = } {conf[0] = }", roi)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Завдання 2
# Напишіть програму по відстеженню об’єкта на відео.
# Відкрийте відео з файлу data\lesson8\animals.mp4 та
# виведіть на екран результат детекції.
# Попросіть користувача ввести ID об’єкта, який потрібно
# відслідковувати
# Для віх наступних кадрів проведіть детекцію, отримайте
# рамку для об’єкта з потрібним ID та виведіть її на екран.
# Додатково показуйте оригінальне відео.
# Скористайтесь для роботи model.track()

import cv2
import ultralytics

model = ultralytics.YOLO("yolo11s.pt")

cap = cv2.VideoCapture('animals.mp4')

success, img = cap.read()

if not success:
    print("Не вдалося відкрити відео")
    exit()

img = cv2.resize(img, None, fx=0.5, fy=0.5)

results = model.track(
    img,
    device="cpu",
    conf=0.25,
    iou=0.5,
    persist=True
)

result = results[0]

cv2.imshow("result", result.plot())
cv2.imshow("orig", img)

object_id = int(input("Введіть ID об'єкта: "))

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    results = model.track(
        frame,
        device="cpu",
        conf=0.25,
        iou=0.5,
        persist=True
    )

    result = results[0]

    boxes = result.boxes

    for i in range(len(boxes)):
        box = boxes[i]

        if box.id is None:
            continue

        id = box.id.cpu().numpy()
        id = int(id[0])

        if id == object_id:
            xyxy = box.xyxy
            xyxy = xyxy.cpu().numpy()
            xyxy = xyxy.astype(int)

            x1, y1, x2, y2 = xyxy[0]

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"ID: {id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    cv2.imshow("result", result.plot())
    cv2.imshow("orig", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()