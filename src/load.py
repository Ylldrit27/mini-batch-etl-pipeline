import sqlite3
from logger import get_logger

logger = get_logger()

def load_data(df):
    """Load cleaned data into SQLite database."""
    
    logger.info("Loading data into SQLite database")
    
    conn = sqlite3.connect("customer_data.db")

    df.to_sql(
        "customers", 
        conn, 
        if_exists="replace", 
        index=False
    )

    conn.close()

    logger.info("Data successfully loaded into database")