# src/main.py
from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Starting ETL pipeline...\n")
    
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
    
    print("\nETL pipeline finished successfully!")

if __name__ == "__main__":
    run_pipeline()