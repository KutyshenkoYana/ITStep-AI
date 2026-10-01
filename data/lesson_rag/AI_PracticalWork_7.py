# Завдання 1
# Напишіть додаток, який симулює спілкування з певною
# відомою людиною.
# З ким саме спілкуватись вводить користувач через
# st.text_input()


import os
import dotenv
import streamlit as st

from langchain_google_genai import ChatGoogleGenerativeAI

dotenv.load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    api_key=gemini_api_key
)

st.title("Спілкування з відомою людиною")

person = st.text_input("З ким ви хочете поспілкуватися?")

if person:
    user_message = st.text_input("Ваше повідомлення:")

    if user_message:
        prompt = f"""
        Ти симулюєш спілкування з відомою людиною {person}.
        Відповідай так, ніби ти ця людина.
        Відповідь повинна відповідати її відомим поглядам,
        стилю спілкування та біографії.

        Повідомлення користувача:
        {user_message}
        """

        response = llm.invoke(prompt)

        st.write(response.content)