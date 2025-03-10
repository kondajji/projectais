import sqlite3

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect("db/ais.db")  # Database file inside `data/`
    conn.row_factory = sqlite3.Row  # Return results as dictionary-like objects
    return conn
