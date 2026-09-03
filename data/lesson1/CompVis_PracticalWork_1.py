# Завдання 1
# Створіть масив з числами від 1 до 10. Виведіть його, його
# розмір, тип даних.
# Змініть розмір масиву на (5, 2). Знову виведіть масив,
# розмір та тип даних

# import numpy as np
#
# # nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# nums = np.arange(1,11)
#
# print(nums)
# print(nums.shape)
# print(nums.dtype)
#
# new_nums = nums.reshape(5,2)
#
# print(new_nums)
# print(new_nums.shape)
# print(new_nums.dtype)


# Завдання 2
# Створіть масив:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# Використовуючи індекси виведіть:
# ● число 7
# ● другий рядок
# ● останній стовпчик
# ● праву половину
# ● жовту область
# ● замініть жовту область на -1
# ● зробіть перший стовпчик таким самим як і другий

# import numpy as np
# nums = np.arange(1,13)
#
# # print(nums)
#
# new_nums = nums.reshape(3,4)

# print(new_nums)

# print(new_nums[1,2])

# print(new_nums[1,:])

# print(new_nums[:,-1])

# print(new_nums[:,2:4])

# print(new_nums[1:3,1:3])

# new_nums[1:3,1:3] = -1
# print(new_nums)

# new_nums[:, 0] = new_nums[:, 1]
# print(new_nums)



# Завдання 3
# У масиві з попереднього завдання створіть маску для
# чисел які більші за 6. З її допомогою
# ● виведіть кількість чисел більших за 6
# ● виведіть самі числа
# ● до кожного числа яке відповідає масці додайте 10
# ● кожне число що не відповідає масці помножте на -1
# ● замініть ці числа які відповідають масці на відповідні
# їм з масиву
# 1 0 1 0
# 0 1 0 1
# 1 0 1 0

# mask = new_nums > 6
# print(new_nums[mask])

# print(mask.sum())

# new_nums[mask] += 10
# print(new_nums)

# new_nums[~mask] *= -1
# print(new_nums)

# other_nums = np.array([
#     [1, 0, 1, 0],
#     [0, 1, 0, 1],
#     [1, 0, 1, 0]
# ])
#
# print(other_nums)
#
# new_nums[mask] = other_nums[mask]
# print(new_nums)



# Завдання 4
# Створіть масив
# -10 24 35
# 250 -6 7
# 12 180 11
# -2 -45 -26
# Усі числа менші за 0 замініть на 0.
# Усі числа більші за 100 замініть на 100

# import numpy as np
# nums = np.array([
#     [-10, 24, 35],
#     [250,-6,7],
#     [12,180,11],
#     [-2,-45,-26]
# ])
#
# print(nums)
#
# mask = nums < 0
# nums[mask] = 0
# # print(nums)
#
# mask2 = nums > 100
# nums[mask2] = 100
# print(nums)

