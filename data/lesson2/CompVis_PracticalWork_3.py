# Завдання 1
# Відкрийте зображення data/lesson2/marbles.png.
# Використайте кольорову сегментацію для отримання масок до
# кульок:
#  синього кольору
#  зеленого і червоного

import cv2
import numpy as np

# image = cv2.imread("marbles.png")
# cv2.imshow("image", image)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# # lower = (100,100,100)
# # upper = (130,255,255)
# #
# # mask1 = cv2.inRange(hsv,lower,upper)
# # cv2.imshow("mask1", mask1)
#
#
# lower = (0,100,150)
# upper = (7,255,255)
#
# mask_red = cv2.inRange(hsv,lower,upper)
#
# lower = (40,90,80)
# upper = (85,255,255)
#
# mask_green = cv2.inRange(hsv,lower,upper)
#
# # cv2.imshow("mask_red", mask_red)
# # cv2.imshow("mask_green", mask_green)
#
# mask_green_red = cv2.bitwise_or(mask_red, mask_green)
#
# # cv2.imshow("green_red_mask",mask_green_red)
#
#
# #  чорного
# #  білого
#
# lower = (0,0,0)
# upper = (50,100,200)
#
# mask_black = cv2.inRange(hsv,lower,upper)
#
# # cv2.imshow("black_mask", mask_black)
#
# lower = (0,0,200)
# upper = (100,30,255)
#
# mask_white = cv2.inRange(hsv,lower,upper)
# # cv2.imshow("white_mask", mask_white)
#
# cv2.waitKey(0)




# Завдання 2
# Відкрийте зображення data/lesson2/cell.png. Покращте
# зображення за допомогою вирівнювання гістограми. Оскільки
# зображення кольорове, вам доведеться зробити наступні
# кроки:
#  перевести зображення в LAB
#  розбити зображення на канали l, a та b
#  вирівняти гістограму для l
#  зібрати канали назад в зображення
#  перевести результат назад в BGR

image = cv2.imread("cell.png")

cv2.imshow("image", image)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)

new_l = cv2.equalizeHist(l)
new_lab = cv2.merge((new_l, a, b))

new_image = cv2.cvtColor(new_lab, cv2.COLOR_LAB2BGR)
cv2.imshow("new_image", new_image)


cv2.waitKey(0)
