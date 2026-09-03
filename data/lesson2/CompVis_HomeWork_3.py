# Завдання 1
# Відкрийте зображення data\lesson2\darken.png. Проведіть з
# ним наступні операції, переведіть його в HSV формат та
# обробіть канал Value наступними способами:
#  застосуйте вирівнювання гістограм
#  збільшіть значення десь на 20-50%, оскільки тут
# результат буде типу float32 та явно вийде за межі [0-255]
# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)
# Виведіть результати обох обробок на екран

import cv2
import numpy as np

image = cv2.imread("darken.png")
cv2.imshow("image", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

new_v = cv2.equalizeHist(v)
new_hsv = cv2.merge((h, s, new_v))

result = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("hsv_result",result)

v_changes = v.astype(np.float32) * 1.3
v_changes = np.clip(v_changes, 0, 255)

v_changes = v_changes.astype(np.uint8)

hsv_changes = cv2.merge((h, s, v_changes))

last_result = cv2.cvtColor(hsv_changes, cv2.COLOR_HSV2BGR)

cv2.imshow("+30%", last_result)



cv2.waitKey(0)