from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import requests

# EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# LOAD VECTOR DB
db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# USER QUESTION
query = input("Ask something: ")

# SEARCH RELEVANT CHUNKS
results = db.similarity_search(query, k=3)

# BUILD CONTEXT
context = "\n\n".join([r.page_content for r in results])

# PROMPT
prompt = f"""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

# SEND TO LM STUDIO
response = requests.post(
    "http://localhost:1234/v1/chat/completions",
    json={
        "model": "google/gemma-4-e4b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.3
    }
)

# GET RESPONSE
answer = response.json()["choices"][0]["message"]["content"]

print("\n")
print("=" * 50)
print("ANSWER:")
print(answer)

print("\n")
print("=" * 50)
print("SOURCES:")

for r in results:
    print(r.metadata.get("source"))