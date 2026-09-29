import os
from dotenv import load_dotenv
from google import genai

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# Завдання 1
# Напишіть чат модель яка підсумовує всю розмову в декілька речень.
# Вкажіть щоб модель зберігала якомога більше деталей.
# Використайте цю модель для простого чат бота який замість trim_massages
# використовує модель з підсумуванням.
# Підсумовуйте повідомлення, коли їх більше 4.
# Старі повідомлення треба видалити
# НЕ ВИДАЛЯТИ SystemMessage та не використовувати його для підсумування


history = [
    {
        "role": "system",
        "content": "Ти корисний чат-бот. Відповідай користувачу чітко та зрозуміло."
    }
]

summary = ""


while True:
    message = input("\nВи: ")

    if message == "":
        break

    history.append({
        "role": "user",
        "content": message
    })

    if len(history) > 5:
        old_messages = history[1:-4]

        text_to_summarize = ""

        if summary != "":
            text_to_summarize += "Попередній підсумок:\n" + summary + "\n\n"

        for item in old_messages:
            text_to_summarize += f"{item['role']}: {item['content']}\n"

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"""
Підсумуй історію розмови в декілька речень.
Збережи якомога більше важливих деталей, фактів, імен,
чисел, побажань користувача та контексту розмови.

Історія:
{text_to_summarize}
"""
        )

        summary = response.text

        history = [history[0]] + history[-4:]


    conversation = ""

    if summary != "":
        conversation += f"Підсумок попередньої розмови:\n{summary}\n\n"

    for item in history:
        conversation += f"{item['role']}: {item['content']}\n"

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=conversation
    )

    answer = response.text

    print("AI:", answer)

    history.append({
        "role": "assistant",
        "content": answer
    })