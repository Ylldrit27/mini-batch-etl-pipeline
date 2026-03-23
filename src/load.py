import sqlite3
from logger import get_logger

logger = get_logger()
DB_PATH = "customer_data.db"
TABLE_NAME = "customers"

def load_data(df):
    """Load cleaned data into SQLite database in an idempotent way."""
    
    logger.info("Loading data into SQLite database (idempotent)")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        age INTEGER,
        signup_date TEXT
    )
    """)

    # Insert data row by row
    for _, row in df.iterrows():
        try:
            cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (id, name, email, age, signup_date)
            VALUES (?, ?, ?, ?, ?)
            """, (row['id'], row['name'], row['email'], row.get('age'), row.get('signup_date')))
        except sqlite3.IntegrityError:
            # Skip duplicates (based on UNIQUE constraint on email)
            logger.info(f"Skipping duplicate record: {row['email']}")
            continue

    conn.commit()
    conn.close()

    logger.info("Data successfully loaded into database (idempotent)")