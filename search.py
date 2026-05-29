from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# LOAD EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# LOAD CHROMA DB
db = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# YOUR QUESTION
query = input("Ask something: ")

# SEARCH
results = db.similarity_search(query, k=3)

# PRINT RESULTS
for i, result in enumerate(results):
    print("\n")
    print(f"Result {i+1}")
    print("-" * 50)
    print(result.page_content)
    print("\nSOURCE:")
    print(result.metadata.get("source"))