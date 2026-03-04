# src/transform.py

def transform_data(df):
    """Apply simple transformations to data."""
    # Example: lowercase all column names
    df.columns = [col.lower() for col in df.columns]
    
    # Example: remove rows with missing 'email'
    if 'email' in df.columns:
        df = df[df['email'].notna()]
    
    print("Data transformed successfully!")
    return df