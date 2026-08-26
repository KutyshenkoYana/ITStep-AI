# Завдання 1
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# розмір зображення, тип даних, максимальну та мінімальну
# інтенсивність пікселів, саме зображення з підписом.

import cv2
import numpy as np

image = cv2.imread(
    "Lenna.png",
    cv2.IMREAD_GRAYSCALE,
)

cv2.imshow("Lenna", image)

print(image.dtype)
print(image.shape)
print(image.max())
print(image.min())




# Завдання 2
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# такі зображень:
#  Верхній лівий кут розміром 100х50
#  Центральний квадрат розміром 100х100
#  Верхню половину
#  Нижню половину
#  Ліву половину
#  Праву половину

# segment1 = image[0:100,0:50]
# cv2.imshow("segment1",segment1)
# print(segment1.shape)
# cv2.waitKey(0)

# segment2 = image[78:178,78:178]
# cv2.imshow("segment2",segment2)
# print(segment2.shape)
# cv2.waitKey(0)

# segment3 = image[:128,:]
# cv2.imshow("segment3",segment3)
# print(segment3.shape)
# cv2.waitKey(0)

# segment4 = image[128:,:]
# cv2.imshow("segment4",segment4)
# print(segment4.shape)
# cv2.waitKey(0)

# segment5 = image[:,:128]
# cv2.imshow("segment5",segment5)
# print(segment5.shape)
# cv2.waitKey(0)

# segment6 = image[:,128:]
# cv2.imshow("segment6",segment6)
# print(segment6.shape)
# cv2.waitKey(0)


# Завдання 3
# Відкрийте зображення data/Lenna.png. Створіть наступні
# зображення

# image[:20,:] = 0
# image[235:255,:] = 255
# cv2.imshow("Lenna", image)
#
# cv2.waitKey(0)


# image[:,:20] = 0
# image[:,235:] = 0
# cv2.imshow("Lenna", image)
#
# cv2.waitKey(0)


# image[:,:40] = 0
# image[:,215:] = 0
# image[:40,:] = 0
# image[215:,:] = 0
# cv2.imshow("Lenna", image)
#
# cv2.waitKey(0)



# Завдання 4
# Відкрийте зображення data/Lenna.png. Створіть маску для
# пік селів з інтенсивністю більше 128 та виведіть її. Також
# виведіть заперечення цієї маски.
# На оригінальному зображенні, усі пікселі які не
# відповідають масці замініть на 0 та виведіть результат

# mask = image > 128
# print(mask)
#
# new_mask = mask.astype(np.uint8)
# cv2.imshow("new_mask",new_mask * 255)
#
# image[~mask] = 0
# cv2.imshow("new_image", image)
#
#
# cv2.waitKey(0)

