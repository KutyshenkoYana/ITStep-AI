import os
from dotenv import load_dotenv
from google import genai

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 1
# Напишіть промпт для створення плану навчального курсу з певної теми
# для цільової айдиторії(початківці, професіонали, діти, тощо).
# Вхідні параметри: тема, опис цільової аудиторії
# Реалізуйте двома способами:
# Zero-shot
# Few-shot


topic = input("Введіть тему курсу: ")
audience = input("Опишіть цільову аудиторію: ")


prompt = f"""
Створи план навчального курсу на тему "{topic}".
Цільова аудиторія: {audience}.

Склади план з основними темами та підтемами.
Врахуй рівень підготовки цільової аудиторії.
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
)

print("\nZero-shot:")
print(response.text)


prompt = f"""
Створи план навчального курсу на задану тему для заданої цільової аудиторії.

Приклад:
Тема: Python
Цільова аудиторія: початківці

План:
1. Вступ до Python
2. Змінні та типи даних
3. Умовні оператори
4. Цикли
5. Функції
6. Робота зі списками та словниками
7. Практичний проєкт

Тепер створи план курсу.

Тема: {topic}
Цільова аудиторія: {audience}

Врахуй рівень підготовки аудиторії та розташуй теми від простих до складніших.
"""

response = client.models.generate_content(
    model="gemini-flash-lite-latest",
    contents=prompt
)

print("\nFew-shot:")
print(response.text)