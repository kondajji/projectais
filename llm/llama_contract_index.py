from llama_index.core import SQLDatabase, Settings
from llama_index.core.indices import GPTSQLStructStoreIndex
from sqlalchemy import create_engine, inspect
from llama_index.llms.openai import OpenAI

# Database path
DB_PATH = "db/ais.db"

# Global variable to store the preloaded index
llama_index = None

def connect_to_db():
    """Establish SQLite connection and check if the 'contracts' table exists."""
    engine = create_engine(f"sqlite:///{DB_PATH}")
    sql_db = SQLDatabase(engine)

    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("📌 Tables in DB:", tables)  # Debugging print

    if "contracts" not in tables:
        print("⚠️ Warning: 'contracts' table not found! Ensure it exists and has data.")

    return sql_db

def preload_index():
    """Preload LlamaIndex at startup for faster queries."""
    global llama_index  # Use global variable
    sql_db = connect_to_db()

    # Set OpenAI LLM
    Settings.llm = OpenAI("gpt-3.5-turbo")

    # Create an index if not already loaded
    if llama_index is None:
        llama_index = GPTSQLStructStoreIndex([], sql_database=sql_db)
        print("✅ LlamaIndex Preloaded Successfully!")

def query_contract_details(question):
    """Query contract details using the preloaded LlamaIndex."""
    global llama_index

    if llama_index is None:
        print("⚠️ LlamaIndex not preloaded! Loading now...")
        preload_index()

    query_engine = llama_index.as_query_engine()
    
    print("🔍 Executing Query:", question)
    response = query_engine.query(question)

    print("📌 LlamaIndex Raw Response:", response)
    return response

# Preload the index at startup
preload_index()

if __name__ == "__main__":
    question = input("Ask about contract details: ")
    response = query_contract_details(question)
    print("\nLlamaIndex Response:", response)
