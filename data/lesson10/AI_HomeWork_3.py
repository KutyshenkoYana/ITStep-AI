import os
from dotenv import load_dotenv
from google import genai

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 1
# Напишіть модель для генерації персонального плану тренувань з двох ланцюгів:
# Перший ланцюг отримує мету тренування(схуднення, набір м’язів, тощо)
# та повертає список вправ
# Другий ланцюг отримує список вправ, рівень підготовки користувача
# (низький, середній, професіонал) та кількість часу на тиждень(в годинах)
# і повертає план тренувань


goal = input("Введіть мету тренування: ")


response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"""
Підбери список вправ для тренувань з метою: {goal}.

Поверни список з 8-10 вправ.
Для кожної вправи напиши тільки її назву.
"""
)

exercises = response.text

print("\nСписок вправ:")
print(exercises)


level = input("\nВведіть рівень підготовки (низький/середній/професіонал): ")
hours = input("Введіть кількість годин на тиждень: ")


response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=f"""
Створи персональний план тренувань.

Мета тренування: {goal}

Список вправ:
{exercises}

Рівень підготовки: {level}
Кількість часу на тиждень: {hours} годин

Склади план тренувань на тиждень.
Розподіли тренування по днях та вкажи вправи, підходи,
повторення та приблизний час тренування.
Врахуй рівень підготовки користувача.
"""
)

print("\nПлан тренувань:")
print(response.text)