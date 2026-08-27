# Завдання 2
# Домашнє завдання
# Виведіть зображення. Підберіть самостійно межі

# import cv2
# import numpy as np
#
# image = cv2.imread(
#     "baboo.jpg",
#     cv2.IMREAD_GRAYSCALE,
# )
#
# cv2.imshow("baboo", image)
#
# segment1 = image[10:50,60:200]
#
# cv2.imshow("segment1", segment1)
#
# cv2.waitKey(0)





# Завдання 1
# Відкрийте зображення data/Lenna.png. Прочитайте маски
# data/mask1.png та data/mask2.png.
# Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or()
# та виведіть результат
# Виведіть ту частину зображення, яка відповідає:
#  mask1
#  mask2
#  mask1 і mask2
# Усі пікселі які не відповідають маскам замінити на 0, перед
# застосуванням змініть тип даних у масці на bool

import cv2
import numpy as np

image = cv2.imread("Lenna.png")

mask1 = cv2.imread("mask1.png", cv2.IMREAD_GRAYSCALE)
mask2 = cv2.imread("mask2.png", cv2.IMREAD_GRAYSCALE)

mask_or = cv2.bitwise_or(mask1, mask2)

mask1_bool = mask1.astype(bool)
mask2_bool = mask2.astype(bool)
mask_or_bool = mask_or.astype(bool)

result_mask1 = np.zeros_like(image)
result_mask2 = np.zeros_like(image)
result_or = np.zeros_like(image)

result_mask1[mask1_bool] = image[mask1_bool]

result_mask2[mask2_bool] = image[mask2_bool]

cv2.imshow("Image", image)
cv2.imshow("Result_mask_1", result_mask1)
cv2.imshow("Result_mask_2", result_mask2)

cv2.waitKey(0)


