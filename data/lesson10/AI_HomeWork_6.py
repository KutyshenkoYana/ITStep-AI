import os
import dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

dotenv.load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    api_key=gemini_api_key,
)

search = GoogleSerperAPIWrapper(
    type="places",
    serper_api_key=serper_api_key
)


def search_restaurants(user_query: str):
    """
    Шукає ресторани за запитом користувача
    та повертає інформацію про назву, сайт і рейтинг.

    :param user_query: запит користувача
    :return: результати пошуку ресторанів
    """
    result = search.results(user_query)

    return result


agent = create_react_agent(
    model=llm,
    tools=[search_restaurants]
)

messages = [
    SystemMessage(
        """
        Ти ввічливий чат-бот для рекомендації ресторанів.

        Використовуй інструмент search_restaurants для пошуку ресторанів.

        Для кожного ресторану показуй:
        - назву
        - посилання на сайт, якщо є
        - рейтинг

        Не вигадуй інформацію, якої немає в результатах пошуку.
        """
    )
]

while True:
    user_query = input("Ви: ")

    if user_query == "":
        break

    human_message = HumanMessage(user_query)

    messages.append(human_message)

    input_data = {
        "messages": messages
    }

    response = agent.invoke(input_data)

    messages = response["messages"]

    answer = messages[-1]

    print(answer.content)