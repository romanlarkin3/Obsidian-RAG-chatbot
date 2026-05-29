from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import os

VAULT_PATH = "PATH_TO_YOUR_VAULT"

documents = []

# LOAD ONLY .md FILES
for root, dirs, files in os.walk(VAULT_PATH):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)

            try:
                loader = TextLoader(path, encoding="utf-8")
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {path}: {e}")

print(f"Loaded {len(documents)} documents")

# SPLIT INTO CHUNKS
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# EMBEDDINGS
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# CREATE VECTOR DB
db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./chroma_db"
)

print("ChromaDB created successfully!")