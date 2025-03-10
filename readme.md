# AIS (AI System for Contract & Software Query Classification)

## Overview
AIS is an AI-driven system designed to classify and process queries related to contracts and software. The system leverages Natural Language Processing (NLP) models to accurately classify queries, retrieve relevant data from an SQLite database, and synthesize responses.

## Project Structure

 - image to be added later


## Technologies Used

- **Python**: Core language for the project.
- **SQLite**: Used for storing contract and software data.
- **LangChain**: Planned for handling LLM-based interactions.
- **Sentence Transformers**: Used for query classification.
- **LlamaIndex (Planned)**: For efficient database querying.
- **Redis (Planned)**: For caching query results and improving performance.

## Progress So Far

1. **Query Classification**
   - Implemented using `sentence-transformers` for semantic similarity.
   - Supports contract-related and software-related queries.

2. **Database Management**
   - SQLite database setup (`ais.db`).
   - Sample contract and software data inserted.

3. **Integration**
   - Query classifier interacts with the database.
   - Response synthesis module under development.

## Next Steps

- Implement LlamaIndex for better database querying.
- Optimize query response time using Redis caching.
- Enhance response generation using LangChain.

---

## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone <repo-url>
   cd PROJECTAIS
