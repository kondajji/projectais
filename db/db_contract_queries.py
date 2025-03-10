import sqlite3
import os

# Ensure the 'db' directory exists
DB_PATH = "db/ais.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_contract_table():
    """Create the contracts table if it does not exist."""
    query = """
    CREATE TABLE IF NOT EXISTS contracts (
        contract_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id INTEGER NOT NULL,
        vendor_name TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        contract_value REAL NOT NULL,
        invoiced_amount REAL NOT NULL,
        payment_status TEXT CHECK(payment_status IN ('Paid', 'Partially Paid', 'Unpaid')),
        contract_status TEXT CHECK(contract_status IN ('Active', 'Expired', 'Cancelled')),
        renewal_date TEXT NULL
    );
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("✅ Contract table created successfully!")

if __name__ == "__main__":
    create_contract_table()
