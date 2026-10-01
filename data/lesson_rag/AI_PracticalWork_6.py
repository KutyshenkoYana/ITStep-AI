# Завдання 1
# Створіть векторну базу даних, де кожен документ – це
# вміст файлу з папки data/lesson_rag/files
#  добавте в метадані шлях до файлу
#  створіть для кожного документу ID
#  збережіть створені ID та назви відповідних файлів в
# окремий json файл
# Перевірте чи працює правильно пошук


import os
import json
import uuid
import dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from pinecone import Pinecone, ServerlessSpec

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

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
    )

index = pc.Index(index_name)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

files_path = os.path.join(
    os.path.dirname(__file__),
    "files"
)

documents = []
files_ids = {}

for file_name in os.listdir(files_path):
    file_path = os.path.join(files_path, file_name)

    if not file_name.endswith(".txt"):
        continue

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    document_id = str(uuid.uuid4())

    document = Document(
        page_content=content,
        metadata={
            "path": file_path,
            "id": document_id
        }
    )

    documents.append(document)

    files_ids[document_id] = file_name

vector_store.add_documents(
    documents=documents,
    ids=[document.metadata["id"] for document in documents]
)

json_path = os.path.join(
    os.path.dirname(__file__),
    "files_ids.json"
)

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        files_ids,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Документи додано до векторної бази даних.")

user_query = input("Пошук: ")

result_docs = vector_store.similarity_search(
    user_query,
    k=2
)

print("\nРезультат пошуку:")

for document in result_docs:
    print()
    print("ID:", document.metadata["id"])
    print("Шлях:", document.metadata["path"])
    print(document.page_content[:500])