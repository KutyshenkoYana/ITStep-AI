# import os
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
#
# load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")
#
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#
#
# # Завдання 1
# # Підключіть модель LLM за допомогою свого API key.
# # Попросіть модель згенерувати:
# # ● відповідь на питання у вигляді одного слова(наприклад яка столиця Франції?)
# # ● код python
# # ● коротку історію
# # Підберіть параметри креативності та довжини
#
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents="Яка столиця Франції? Відповідай тільки одним словом.",
#     config=types.GenerateContentConfig(
#         temperature=0.2,
#         max_output_tokens=10
#     )
# )
#
# print("Відповідь на питання:")
# print(response.text)
#
#
#
# response = client.models.generate_content(
#     model="gemini-flash-lite-latest",
#     contents="Напиши коротку цікаву історію про дівчину, яка знайшла старий ключ.",
#     config=types.GenerateContentConfig(
#         temperature=1.0,
#         max_output_tokens=200
#     )
# )
#
# print("\nКоротка історія:")
# print(response.text)





import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 2
# Прочитайте файл data\lesson9\rules.txt з правилами користування атракціону.
# Напишіть програму яка отримує від користувачі питання та дає відповідь на нього
# виходячи з текстового файлу.
# Для цього об’єднайте правила користування з питанням користувача.
# Користувач задає питання поки не введе порожній рядок.
# Змініть файл rules.txt, щоб переконатись що модель дійсно його читає.


with open("rules.txt", "r", encoding="utf-8") as file:
    rules = file.read()


while True:
    question = input("\nВаше питання: ")

    if question == "":
        break

    prompt = f"""
Правила користування атракціоном:

{rules}

Питання користувача:
{question}

Відповідай на питання тільки на основі правил.
Якщо відповіді на питання немає в правилах, напиши:
"У правилах немає такої інформації."
"""

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=150
        )
    )

    print("Відповідь:")
    print(response.text)