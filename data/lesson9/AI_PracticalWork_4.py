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
# # Напишіть чат бота, який спілкується у стилі різних персонажів книг,
# # фільмів або відомих людей.
# # Ким саме бути чат бот вирішує з повідомлення від користувача.
# # Якщо персонаж або книга невідомі, то відповісти що невідома інформація
# # та запропонувати декілька відомих прикладів на вибір
#
#
# character = input("Ким має бути чат-бот? ")
#
# history = []
#
#
# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=f"""
# Користувач хоче, щоб чат-бот спілкувався у стилі: {character}.
#
# Якщо ти знаєш цього персонажа, книгу, фільм або відому людину,
# коротко опиши стиль спілкування та використовуй його надалі.
#
# Якщо інформація тобі невідома, напиши:
# "Невідома інформація."
# Після цього запропонуй декілька відомих персонажів або людей на вибір.
# """
# )
#
# style = response.text
#
# print("\nAI:", style)
#
#
# while True:
#     message = input("\nВи: ")
#
#     if message == "":
#         break
#
#     history.append(f"Human: {message}")
#
#     prompt = f"""
# Ти чат-бот, який спілкується у стилі {character}.
#
# Інформація про стиль:
# {style}
#
# Історія діалогу:
# {chr(10).join(history)}
#
# Відповідай у відповідному стилі.
# """
#
#     response = client.models.generate_content(
#         model="gemini-3.1-flash-lite",
#         contents=prompt
#     )
#
#     answer = response.text
#
#     print("AI:", answer)
#
#     history.append(f"AI: {answer}")





import os
from dotenv import load_dotenv
from google import genai

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 2
# Напишіть чат бота, який дає відповіді на питання стосовно умов
# повернення товару.
# Якщо користувач запитує щось інше, то відповідати що немає інформації.
# Застосуйте обмеження історії(можна десь 5 повідомлень)


file_path = os.path.join(os.path.dirname(__file__), "return_policy.txt")

with open(file_path, "r", encoding="utf-8") as file:
    rules = file.read()


history = []


while True:
    message = input("\nВаше питання: ")

    if message == "":
        break

    history.append(f"Human: {message}")
    history = history[-5:]

    prompt = f"""
Ти чат-бот, який відповідає тільки на питання про умови
повернення товару.

Правила повернення товару:
{rules}

Історія діалогу:
{chr(10).join(history)}

Якщо питання стосується повернення товару,
відповідай тільки на основі правил.

Якщо питання не стосується повернення товару,
відповідай:
"У мене немає інформації з цього питання."
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    answer = response.text

    print("AI:", answer)

    history.append(f"AI: {answer}")
    history = history[-5:]