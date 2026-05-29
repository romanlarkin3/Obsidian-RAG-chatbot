# Obsidian-RAG-chatbot

Local Retrieval-Augmented Generation (RAG) chatbot for Obsidian notes. The project uses Sentence Transformers for embeddings, ChromaDB for vector search, and LM Studio for local LLM inference. It supports semantic search, contextual question answering, and source note retrieval over a personal knowledge base.

---

## 📌 Project Documentation

A detailed project description, architecture explanation, code walkthrough, and implementation details are available in the accompanying PDF document.

### Language Versions

* **Pages 1–10:** English 🇬🇧
* **Pages 10–20:** Ukrainian 🇺🇦

The PDF includes:

* project overview;
* RAG architecture explanation;
* indexing workflow;
* semantic search workflow;
* chatbot workflow;
* source code explanations;
* technology stack;
* implementation details.

---

## ✨ Features

* Semantic search across Obsidian notes
* Retrieval-Augmented Generation (RAG)
* Local LLM integration via LM Studio
* ChromaDB vector database
* Sentence Transformers embeddings
* Markdown note ingestion
* Source note retrieval
* Fully local execution
* No external AI APIs required

---

## 🏗️ Architecture

```text
Obsidian Notes (.md)
        ↓
ingest.py
        ↓
Sentence Transformers
        ↓
ChromaDB
        ↓
search.py
        ↓
chatbot.py
        ↓
LM Studio
        ↓
Generated Answer
```

---

## ⚙️ Technology Stack

* Python
* LangChain
* ChromaDB
* Sentence Transformers
* LM Studio
* Local LLMs
* Obsidian

---

## 🚀 How It Works

### 1. Indexing

The `ingest.py` script:

* loads markdown notes from an Obsidian Vault;
* splits notes into chunks;
* generates embeddings;
* stores embeddings in ChromaDB.

### 2. Semantic Search

The `search.py` script:

* converts user queries into embeddings;
* performs similarity search;
* retrieves relevant chunks from the vector database.

### 3. Answer Generation

The `chatbot.py` script:

* retrieves relevant context;
* sends context to a local LLM through LM Studio;
* generates contextual answers;
* returns source notes used during retrieval.

---

## 📄 Documentation

For a complete explanation of the project, please refer to:

```text
documentation/Obsidian RAG chatbot.pdf
```

English version: Pages 1–10
Ukrainian version: Pages 10–20
