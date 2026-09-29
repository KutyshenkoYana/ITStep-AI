import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\.env")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 1
# Прочитайте файл data\lesson9\return_policy.txt
# Та напишіть простий чат бот для відповідей на питання користувачів
# стосовно повернення товару.
# Діалог завершується коли користувач вводить порожній рядок.
# Передавайте усю історію спілкування у форматі:
# Instruction: ….
# Human: massage1
# AI: message2
# Human: massage3
# AI: message4
# Human: massage5
# AI:


with open(r"C:\Users\jkuty\OneDrive\Documents\ITStep-AI\data\lesson9\return_policy.txt", "r", encoding="utf-8") as file:
    rules = file.read()


history = f"Instruction: Відповідай на питання користувача стосовно повернення товару, використовуючи інформацію з правил:\n{rules}\n"


while True:
    question = input("\nВаше питання: ")

    if question == "":
        break

    history += f"\nHuman: {question}\nAI:"

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=history,
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=200
        )
    )

    answer = response.text

    print("AI:", answer)

    history += f" {answer}"