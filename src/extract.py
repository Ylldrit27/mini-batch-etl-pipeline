# src/extract.py
import os
import pandas as pd

def extract_data():
    """Read raw CSV data."""
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(current_dir, "..", "data", "raw_customers.csv")
    
    df = pd.read_csv(data_path)
    print("Data extracted successfully! First 5 rows:")
    print(df.head())
    return df