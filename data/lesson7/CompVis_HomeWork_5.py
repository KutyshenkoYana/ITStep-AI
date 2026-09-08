# Завдання 1
# Відкрийте відео з файлу data\lesson7\meter.mp4.
# Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через bilateralFilter

import cv2

cap = cv2.VideoCapture("meter.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out_writer = cv2.VideoWriter(
    "result.mp4",
    fourcc,
    fps,
    (500, 500),
    isColor=False
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

    blur = cv2.bilateralFilter(
        gray,
        3,
        30,
        30
    )

    binary = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        21,
        5
    )

    cv2.imshow("binary", binary)

    out_writer.write(binary)

    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

out_writer.release()
cap.release()
cv2.destroyAllWindows()
