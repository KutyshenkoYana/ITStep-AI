# Завдання 1
# Добавте в створену базу даних файл
# data/lesson_rag/huge_file.txt про умови користування гуглом
# Оскільки файл надто великий, то його треба добавляти
# частинами. Для цього:
#  прочитайте вміст файлу
#  розділіть його на окремі блоки(між блоками два
# порожніх рядка, дивись файл)
#  отримайте перший рядок кожного блоку – це його
# назва
#  створіть документи для кожного блоку. В метаданих:
# o назва файлу
# o назва блоку
#  створіть ID та добавте все в існуючу базу даних
#  добавте ID у json файл
#  перевірте агента


import os
import json
import uuid
import re
import dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from pinecone import Pinecone
from langgraph.prebuilt import create_react_agent

dotenv.load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=gemini_api_key,
    output_dimensionality=768
)

pc = Pinecone(api_key=pinecone_api_key)

index_name = "lesson-rag"

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

huge_file_path = os.path.join(
    os.path.dirname(__file__),
    "huge_file.txt"
)

with open(huge_file_path, "r", encoding="utf-8") as file:
    content = file.read()

blocks = re.split(r"\r?\n\s*\r?\n\s*\r?\n", content)

documents = []
document_ids = []

json_path = os.path.join(
    os.path.dirname(__file__),
    "files_ids.json"
)

if os.path.exists(json_path):
    with open(json_path, "r", encoding="utf-8") as file:
        files_ids = json.load(file)
else:
    files_ids = {}

for block in blocks:
    block = block.strip()

    if block == "":
        continue

    lines = block.splitlines()
    block_name = lines[0].strip()

    document_id = str(uuid.uuid4())

    document = Document(
        page_content=block,
        metadata={
            "file_name": "huge_file.txt",
            "block_name": block_name
        }
    )

    documents.append(document)
    document_ids.append(document_id)

    files_ids[document_id] = {
        "file_name": "huge_file.txt",
        "block_name": block_name
    }

vector_store.add_documents(
    documents=documents,
    ids=document_ids
)

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        files_ids,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Документи додано до векторної бази даних.")

def search_doc(user_query: str):
    """
    Шукає інформацію у векторній базі даних
    """
    result_docs = vector_store.similarity_search(
        user_query,
        k=2
    )
    return result_docs

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    api_key=gemini_api_key
)

agent = create_react_agent(
    model=llm,
    tools=[search_doc]
)

while True:
    user_query = input("Ви: ")

    if user_query == "":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        }
    )

    messages = response["messages"]
    answer = messages[-1]

    print(answer.content)
    print()