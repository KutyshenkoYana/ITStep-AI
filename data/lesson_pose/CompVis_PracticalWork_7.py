import cv2
import ultralytics

# Завдання 1
# Відкрийте відео data/lesson_pose/sitting.mp4
# Отримайте перший кадр
# Покажіть його, за потреби змініть розмір

cap = cv2.VideoCapture("sitting.mp4")

success, img = cap.read()

if not success:
    print("Не вдалося відкрити відео")
    cap.release()
    exit()

img = cv2.resize(img, (800, 600))

cv2.imshow("first frame", img)

# Завдання 2
# Застосуйте модель YOLO Pose
# Отримайте результати (result) та виведіть їх на екран
# Використайте параметри device

model = ultralytics.YOLO("../lesson_seg/yolo11s-pose.pt")

results = model.predict(
    img,
    device="cpu"
)

result = results[0]

print(result)

# Завдання 3
# Користуючись методом plot() отримайте зображення з рамками
# та підписами і покажіть його

res_img = result.plot()

cv2.imshow("result", res_img)

# Завдання 4
# Отримайте інформацію про ключові точки(keypoints)
# Виведіть її на екран
# Отримайте координати точок(xy)
# Виведіть координати на екран разом з типом даних та розміром
# позбудьтесь тензорів за допомогою cpu() та numpy()

keypoints = result.keypoints

print(keypoints)

xy = keypoints.xy

xy = xy.cpu().numpy()

print(xy)
print(xy.dtype)
print(xy.shape)

# Завдання 5
# Отримайте координати для лівого коліна, лівої руки,
# правої руки для першого об’єкта
# Намалюйте ці точки на зображенні:
# ліве коліно – зелений
# ліва рука – червоний
# права рука – білий

if len(xy) > 0:

    xy = xy[0]

    xy = xy.astype(int)

    x_left_knee, y_left_knee = xy[13]
    x_left_hand, y_left_hand = xy[9]
    x_right_hand, y_right_hand = xy[10]

    print("Left Knee:", x_left_knee, y_left_knee)
    print("Left Hand:", x_left_hand, y_left_hand)
    print("Right Hand:", x_right_hand, y_right_hand)

    cv2.circle(
        img,
        center=(x_left_knee, y_left_knee),
        radius=15,
        color=(0, 255, 0),
        thickness=-1
    )

    cv2.circle(
        img,
        center=(x_left_hand, y_left_hand),
        radius=15,
        color=(0, 0, 255),
        thickness=-1
    )

    cv2.circle(
        img,
        center=(x_right_hand, y_right_hand),
        radius=15,
        color=(255, 255, 255),
        thickness=-1
    )

    cv2.imshow("points", img)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()



