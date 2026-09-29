# import os
# from dotenv import load_dotenv
# from google import genai
#
# load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")
#
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#
#
# # Завдання 1
# # Напишіть промпт для генерації коду функції для вирішення певної задачі.
# # Вхідні параметри – мова програмування, опис задачі
# # Реалізуйте двома способами:
# # Zero-shot
# # Few-shot
#
#
# language = input("Введіть мову програмування: ")
# task = input("Опишіть задачу: ")
#
#
# prompt = f"""
# Напиши функцію мовою програмування {language}.
# Завдання: {task}
# Поверни тільки код функції без пояснень.
# """
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents=prompt
# )
#
# print("\nZero-shot:")
# print(response.text)
#
#
# prompt = f"""
# Напиши функцію мовою програмування {language} для вирішення задачі: {task}
#
# Приклад:
# Мова: Python
# Завдання: знайти суму двох чисел
# Код:
# def add(a, b):
#     return a + b
#
# Тепер створи функцію для заданої задачі.
# Поверни тільки код функції без пояснень.
# """
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents=prompt
# )
#
# print("\nFew-shot:")
# print(response.text)



import os
from dotenv import load_dotenv
from google import genai

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 2
# Напишіть промпт для переведення тексту з неформального стилю в формальний
# Вхідні параметри – текст
# Реалізуйте двома способами:
# Zero-shot
# Few-shot


text = input("Введіть неформальний текст: ")


prompt = f"""
Перетвори цей текст з неформального стилю у формальний:

{text}

Збережи зміст тексту.
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
)

print("\nZero-shot:")
print(response.text)


prompt = f"""
Перетвори текст з неформального стилю у формальний.

Приклад:
Неформальний: Привіт, можеш скинути мені файл?
Формальний: Добрий день. Чи могли б Ви надіслати мені файл?

Тепер перетвори цей текст:
{text}

Збережи зміст тексту та використай формальний стиль.
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
)

print("\nFew-shot:")
print(response.text)
