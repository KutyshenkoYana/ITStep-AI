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
# # Напишіть модель для рекомендації книг з двох ланцюгів:
# # Перший ланцюг отримує назву книги та визначає її жанр
# # Другий отримує назву книги, жанр та повертає список схожих книг
# # (того ж самого жанру та іншого)
#
#
# book = input("Введіть назву книги: ")
#
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents=f"""
# Визнач жанр книги "{book}".
# Відповідай коротко, тільки назвою жанру.
# """
# )
#
# genre = response.text
#
# print("\nЖанр книги:")
# print(genre)
#
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents=f"""
# Книга: {book}
# Жанр: {genre}
#
# Порекомендуй 5 схожих книг.
# Включи книги того самого жанру та книги інших жанрів,
# які можуть сподобатися читачу цієї книги.
# Для кожної книги напиши її назву та автора.
# """
# )
#
# print("\nРекомендовані книги:")
# print(response.text)




import os
from dotenv import load_dotenv
from google import genai

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 2
# Напишіть модель для генерації листа:
# Перший ланцюг отримує короткий опис листа та генерує основний зміст
# Другий ланцюг отримує основний зміст та стиль листа
# (формальний, неформальний, тощо) та генерує лист


description = input("Введіть короткий опис листа: ")


response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=f"""
На основі короткого опису створи основний зміст листа.

Опис:
{description}

Напиши тільки основний зміст листа без привітання та підпису.
"""
)

content = response.text

print("\nОсновний зміст:")
print(content)


style = input("\nВведіть стиль листа (формальний/неформальний): ")


response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=f"""
Створи готовий лист на основі основного змісту.

Основний зміст:
{content}

Стиль листа:
{style}

Додай відповідне привітання та завершення листа.
Збережи зміст та використай вказаний стиль.
"""
)

print("\nГотовий лист:")
print(response.text)