import sqlite3

DB_PATH = "db/ais.db"

def insert_sample_contracts():
    """Insert sample contract data into the contracts table."""
    contracts = [
        (1, "Smartsheet", "2023-01-01", "2024-12-31", 50000, 25000, "Partially Paid", "Active", "2024-12-01"),
        (2, "Asana", "2022-05-15", "2025-05-14", 75000, 75000, "Paid", "Active", "2025-04-30"),
        (3, "Airtable", "2021-09-01", "2024-08-31", 30000, 10000, "Partially Paid", "Expired", None),
    ]

    query = """
    INSERT INTO contracts (vendor_id, vendor_name, start_date, end_date, contract_value, invoiced_amount, payment_status, contract_status, renewal_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.executemany(query, contracts)
    conn.commit()
    conn.close()
    print("✅ Sample contract data inserted successfully!")

if __name__ == "__main__":
    insert_sample_contracts()
