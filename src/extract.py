import os
import pandas as pd
from logger import get_logger

logger = get_logger()

def extract_data():
    """Read raw CSV data."""
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "..", "data", "raw_customers.csv")
    
    logger.info("Reading raw dataset")

    df = pd.read_csv(data_path)

    logger.info(f"Extracted {len(df)} rows")

    return df