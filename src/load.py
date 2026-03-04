# src/load.py
import os

def load_data(df):
    """Save transformed data to output folder."""
    current_dir = os.path.dirname(__file__)
    output_path = os.path.join(current_dir, "..", "output", "transformed_customers.csv")
    
    # Make sure output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Data loaded successfully! Saved to {output_path}")