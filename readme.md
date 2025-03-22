# AIS (AI System for Contract & Software Query Classification)

## Overview  
AIS is an AI-driven system designed to classify and process queries related to contracts and software. It leverages **Natural Language Processing (NLP)** and **retrieval-augmented generation (RAG)** to classify queries, retrieve relevant data from a **SQLite database**, and generate meaningful responses using **LlamaIndex** and **LangChain**.

---

## Project Structure  

- **Query Classifier**: Categorizes user queries into **contract-related**, **software-related**, or **other** using **Sentence Transformers**.  
- **Data Extractor (LlamaIndex)**: Connects to the database and retrieves relevant contract details efficiently.  
- **Response Synthesizer**: Constructs human-like responses using **LangChain**.  
- **LLM Handler**: Orchestrates query classification, data retrieval, and response generation.  



---

##  Technologies Used  

- **Python**: Core language for development.  
- **SQLite**: Stores contract and software data.  
- **LangChain**: Handles response generation from structured data.  
- **Sentence Transformers**: Performs query classification via semantic similarity.  
- **LlamaIndex**: Extracts structured contract data from the database.  
- **Redis**: Caches query results to optimize response times.  

---

##  Progress So Far  

1️⃣ **Query Classification**  
✔ Implemented using `sentence-transformers` for NLP-based query matching.  
✔ Classifies queries as **contract-related, software-related, or other**.  

2️⃣ **Database Management**  
✔ SQLite database (`ais.db`) configured with contract and software data.  
✔ Tables structured for efficient querying.  

3️⃣ **LlamaIndex Integration**  
✔ Integrated **LlamaIndex** to extract contract details dynamically.  
✔ Queries no longer require predefined SQL queries.  

4️⃣ **Response Generation**  
✔ Implemented response synthesis using **LangChain**.  
✔ Generates user-friendly responses based on retrieved data.  

---

## Next Steps  

- Enhance response accuracy with **vector search** in LlamaIndex.  
- Optimize performance by improving **Redis caching strategy**.  
- Extend support for **multi-table queries** and **metadata filtering**.  

---

## Setup & Installation  

### 1️⃣ Clone the Repository  
```sh
git clone <repo-url>
cd PROJECTAIS
