# Завдання 1
# Відкрийте зображення data/lesson3/notes.png. Проведіть
# наступні дії:
#  проведіть бінарізацію(звичайну та адаптивну)
#  застосуйте розмиття(гаусове) візьміть ядра 3, 5, 11 та
# sigmaX 0, 2, 10
#  повторіть бінарізацію, але перед тим застосуйте bilateral
# filter

# import cv2
# import utils
#
#
# img = cv2.imread("notes.png")
# img = cv2.resize(img, (600,600))
#
# # cv2.imshow("original", img)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("gray", gray)
#
# # threshold = 128
# #
# # mask = gray < threshold
# # gray[mask] = 0
# # gray[~mask] = 255
#
# # cv2.imshow("binary", gray)
#
# # gauss = cv2.GaussianBlur(
# #     gray,  # зображення з шумом
# #     (3,3),   # розмір фільтру(ядра)
# #     sigmaX=1.5,    # наскільки важливими є далекі пікселі  0 - адаптивне
# # )
# #
# #
# # cv2.imshow("gauss", gauss)
#
#
#
# # двосторонній фільтр
# bilat = cv2.bilateralFilter(
#     gray,  # зображення з шумом
#     d=5,    # розмір фільтру
#     sigmaColor=75,   # наскільки важливі пікселі іншого кольору
#     sigmaSpace=75,   # наскільки важливими є далекі пікселі
# )
#
# cv2.imshow("bilat", bilat)
#
#
# res = cv2.adaptiveThreshold(
#     bilat,   # зображення з текстом(чорнобіле)
#     255,    #  білий колір
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
#     cv2.THRESH_BINARY,   # це просто треба вказати
#     11,   # розмір фільтру
#     2,          # наскільки піксель має відрізнятися від порогу
# )
#
#
# cv2.imshow("adaptive", res)
#
#
#
# cv2.waitKey(0)




# Завдання 2
# Відкрийте зображення data/lesson3/sudoku.jpg. Проведіть
# для нього бінарізацію, а саме
#  CLAHE
#  гаусове розмиття
#  адаптивна бінарізація
#  NLMean
# Самостійно підберіть параметри, збережіть результат.
# Порівняйте результати для гаусової та середньої адаптивної
# бінарізації


import cv2
from sympy.codegen.ast import none

import utils


img = cv2.imread("sudoku.jpg")
img = cv2.resize(img, (600,600))

# cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
result = clahe.apply(gray)

# cv2.imshow("clahe", result)


gauss = cv2.GaussianBlur(
    gray,  # зображення з шумом
    (5,5),   # розмір фільтру(ядра)
    sigmaX=5,    # наскільки важливими є далекі пікселі  0 - адаптивне
)

# cv2.imshow("gauss", gauss)

res = cv2.adaptiveThreshold(
    result,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)


cv2.imshow("clahe+adaptive", res)


res = cv2.adaptiveThreshold(
    gauss,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)


cv2.imshow("gauss+adaptive", res)


result_gray = cv2.fastNlMeansDenoising(gray, None, h=10, templateWindowSize=7, searchWindowSize=21)
cv2.imshow("NLmean", result_gray)


res2 = cv2.adaptiveThreshold(
    result_gray,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    11,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)


cv2.imshow("NLmean+adaptive", res2)

cv2.waitKey(0)


