# import os
# import re
# from dotenv import load_dotenv
# from google import genai
#
# load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
#
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#
#
# # Завдання 1
# # Напишіть функцію яка перевіряє складність паролю:
# # кількість символів(>8)
# # наявність хоча б однієї літери\цифри\спеціального символу
# # наявність літер в різних регістрах
# # Функція повертає тест з описом паролю(що добре, а що погано)
# # На основі цієї функції створіть агента
#
#
# def check_password(password):
#     result = []
#
#     if len(password) > 8:
#         result.append("Добре: пароль має більше 8 символів.")
#     else:
#         result.append("Погано: пароль має містити більше 8 символів.")
#
#     if re.search(r"[A-Za-zА-Яа-я]", password):
#         result.append("Добре: є літери.")
#     else:
#         result.append("Погано: немає літер.")
#
#     if re.search(r"\d", password):
#         result.append("Добре: є цифри.")
#     else:
#         result.append("Погано: немає цифр.")
#
#     if re.search(r"[^A-Za-zА-Яа-я0-9]", password):
#         result.append("Добре: є спеціальний символ.")
#     else:
#         result.append("Погано: немає спеціального символу.")
#
#     if re.search(r"[a-zа-я]", password) and re.search(r"[A-ZА-Я]", password):
#         result.append("Добре: є літери в різних регістрах.")
#     else:
#         result.append("Погано: немає літер у різних регістрах.")
#
#     return "\n".join(result)
#
#
# password = input("Введіть пароль: ")
#
# result = check_password(password)
#
# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=f"""
# Ти агент для перевірки складності паролів.
#
# Результат перевірки паролю:
# {result}
#
# Поясни користувачу результат перевірки простими словами.
# Не показуй сам пароль.
# """
# )
#
# print("\nРезультат:")
# print(response.text)




