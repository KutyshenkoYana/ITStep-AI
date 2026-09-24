# Завдання 1
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/crop-seg.jpg
# Покажіть усі маски рослин з підписами назви цієї
# рослини.
# Покажіть також самі рослини, для цього застосуйте
# маску, і всі зайві пікселі замініть на 255(зробити білий фон)

# from ultralytics import YOLO
# import numpy as np
# import cv2
#
# model = YOLO("crop-seg.pt")
#
# img = cv2.imread("crop3.jpg")
# cv2.imshow("orig", img)
#
# results = model.predict(
#     img,
#     device="cpu",
# )
#
# result = results[0]
#
# masks = result.masks
# boxes = result.boxes
#
# masks_data = masks.data
#
# names = result.names
#
# res = result.plot()
# cv2.imshow("plants", res)
#
# for i in range(len(masks_data)):
#
#     mask = masks_data[i]
#
#     mask = mask.cpu().numpy()
#     mask = mask.astype(np.uint8)
#     mask *= 255
#
#     mask = cv2.resize(
#         mask,
#         (img.shape[1], img.shape[0])
#     )
#
#     mask = mask.astype(bool)
#
#     plant = np.ones_like(img) * 255
#
#     plant[mask] = img[mask]
#
#     class_id = int(boxes.cls[i])
#     plant_name = names[class_id]
#
#     cv2.putText(
#         plant,
#         plant_name,
#         (20, 40),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         1,
#         (0, 0, 0),
#         2
#     )
#
#     cv2.imshow("plant " + str(i + 1), plant)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



