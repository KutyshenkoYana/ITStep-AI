# Завдання 1
# Відкрийте зображення data/lesson_seg/tumor1.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/brain-tumor-seg.jpg
# Визначте площу пухлини в пікселях.
# Визначте площу в
# (1 піксель – 0,0025
# )
# В залежності від площі присвойте пухлині певний тип
#  <10 – small
#  10-25 – middle
#  >25 – large
# Покажіть пухлину – за допомогою маски усі лишні
# пікселі зробіть 0, а як назву зображення використайте її тип


from ultralytics import YOLO
import numpy as np
import cv2

model = YOLO("brain-tumor-seg.pt")

img = cv2.imread("tumor1.jpg")
cv2.imshow("orig", img)

results = model.predict(
    img,
    device="cpu",
)

result = results[0]

masks = result.masks
masks_data = masks.data

mask = masks_data[0]

mask = mask.cpu().numpy()
mask = mask.astype(np.uint8)
mask *= 255

mask = cv2.resize(
    mask,
    (img.shape[1], img.shape[0])
)

area_pixels = np.sum(mask > 0)

print("Площа пухлини в пікселях:", area_pixels)

area = area_pixels * 0.0025

print("Площа пухлини:", area)

if area < 10:
    tumor_type = "small"
elif area <= 25:
    tumor_type = "middle"
else:
    tumor_type = "large"

print("Тип пухлини:", tumor_type)

mask = mask.astype(bool)

tumor = np.zeros_like(img)

tumor[mask] = img[mask]

cv2.imshow(tumor_type, tumor)

cv2.waitKey(0)
cv2.destroyAllWindows()