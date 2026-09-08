# Завдання 1
# Виведіть відео з файлу data\lesson7\text.mp4 на екран та
# збережіть в новий файл.
# Змініть розмір зображення.

import cv2

cap = cv2.VideoCapture(
    "text.mp4",
)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_writer = cv2.VideoWriter(
    "result.mp4",   # файл куди зберігати відео
    fourcc,      # кодек
    fps,         # частота кадрів в секунду
    (500,500),   # розмір (ширина, висота)
    isColor=True,   # чи є зображення кадрів кольоровими
)

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(
        frame,
        (500, 500)
    )

    cv2.imshow("res", new_frame)

    out_writer.write(new_frame)

    cv2.waitKey(15)



out_writer.release()
cap.release()


# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.

cap = cv2.VideoCapture("text.mp4")

out_writer = cv2.VideoWriter(
    "result2.mp4",
    fourcc,
    fps,
    (500,500),
    isColor=False,
)

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(
        frame,
        (500, 500)
    )

    gray = cv2.cvtColor(
        new_frame,
        cv2.COLOR_BGR2GRAY
    )

    adapt = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    cv2.imshow("binary", adapt)

    out_writer.write(adapt)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

out_writer.release()
cap.release()



# Завдання 3
# Відкрийте відео з файлу data\lesson7shapes.mp4.
# Проведіть виділення країв на кадрах та збережіть в новий
# файл.


cap = cv2.VideoCapture("shapes.mp4")

out_writer = cv2.VideoWriter(
    "result3.mp4",
    fourcc,
    fps,
    (500,500),
    isColor=False,
)

while True:
    success, frame = cap.read()

    if not success:
        break

    new_frame = cv2.resize(
        frame,
        (500, 500)
    )

    gray = cv2.cvtColor(
        new_frame,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    cv2.imshow("edges", edges)

    out_writer.write(edges)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

out_writer.release()
cap.release()



