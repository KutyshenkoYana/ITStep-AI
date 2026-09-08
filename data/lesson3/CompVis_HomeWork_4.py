# Завдання 1
# Відкрийте зображення data/lesson3/sonet.png. Проведіть
# бінарізацію.
# Обов’язково використайте:
#  розмиття або наведення різкості
#  адаптивну бінарізацію
#  очищеня шумів


import cv2
import utils


img = cv2.imread("sonet.png")
img = cv2.resize(img, (600, 600))

# cv2.imshow("original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray", gray)


gauss = cv2.GaussianBlur(
    gray,
    (3,3),
    sigmaX=2
)

# cv2.imshow("gauss", gauss)


res = cv2.adaptiveThreshold(
    gauss,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

# cv2.imshow("adaptive", res)


result = cv2.fastNlMeansDenoising(
    res,
    None,
    h=10,
    templateWindowSize=7,
    searchWindowSize=21
)

# cv2.imshow("clean", result)





# Завдання 2
# Відкрийте зображення data/lesson3/sonnet_noised.png.
# Проведіть бінарізацію.
# Застосуйте код з завдання 1 та
# спробуйте покращити результат.


import cv2
import utils


img2 = cv2.imread("sonet_noised.png")

# cv2.imshow("original", img2)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray", gray2)


# gauss2 = cv2.GaussianBlur(
#     gray2,
#     (3,3),
#     sigmaX=1.5
# )

# cv2.imshow("gauss", gauss2)


# res2 = cv2.adaptiveThreshold(
#     gauss2,
#     255,
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     cv2.THRESH_BINARY,
#     11,
#     2
# )
#
# cv2.imshow("adaptive", res2)


# result2 = cv2.fastNlMeansDenoising(
#     res,
#     None,
#     h=10,
#     templateWindowSize=7,
#     searchWindowSize=21
# )
#
# cv2.imshow("clean", result2)


clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

result2 = clahe.apply(gray2)

cv2.imshow("clahe", result2)


result2 = cv2.fastNlMeansDenoising(
    gray2,
    None,
    h=7,
    templateWindowSize=7,
    searchWindowSize=21
)

cv2.imshow("NLmean", result2)


gauss2 = cv2.GaussianBlur(
    result2,
    (3, 3),
    sigmaX=1
)

cv2.imshow("gauss", gauss2)


res2 = cv2.adaptiveThreshold(
    gauss2,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow("adaptive", res2)


cv2.waitKey(0)
