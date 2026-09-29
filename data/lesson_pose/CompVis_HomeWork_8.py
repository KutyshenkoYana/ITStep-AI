import cv2
import ultralytics
import utils

# Завдання 1
# Відкрийте відео data/lesson_pose/squat.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки.
# Отримайте координати 3-ох точок ноги.
# Визначте кут між цими трьома точками.
# Скористайтесь функцією utils.get_angle(x1, y1, x2, y2, x3, y3)
# де x2, y2 – координати коліна(центральна точка).
# Запустіть відео та добавте на сам кадр кут згинання ніг.
# Визначіть нижню межу кута
# та верхню межу кута.
# Добавте кількість присідань та кут на кожен кадр.

model = ultralytics.YOLO("yolo11s-pose.pt")

cap = cv2.VideoCapture("squat.mp4")

squat_count = 0
is_down = False

while True:

    success, img = cap.read()

    if not success:
        break

    results = model.predict(
        img,
        device="cpu"
    )

    result = results[0]

    keypoints = result.keypoints

    if keypoints is not None:

        xy = keypoints.xy

        xy = xy.cpu().numpy()

        if len(xy) > 0:

            xy = xy[0]

            xy = xy.astype(int)

            x1, y1 = xy[11]
            x2, y2 = xy[13]
            x3, y3 = xy[15]

            angle = utils.get_angle(
                x1, y1,
                x2, y2,
                x3, y3
            )

            if angle < 90:
                is_down = True

            if angle > 160 and is_down:
                squat_count += 1
                is_down = False

            cv2.circle(
                img,
                (x1, y1),
                10,
                (255, 0, 0),
                -1
            )

            cv2.circle(
                img,
                (x2, y2),
                10,
                (0, 255, 0),
                -1
            )

            cv2.circle(
                img,
                (x3, y3),
                10,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                img,
                "Angle: " + str(int(angle)),
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2
            )

            cv2.putText(
                img,
                "Squats: " + str(squat_count),
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                2
            )

    cv2.imshow("squat", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()