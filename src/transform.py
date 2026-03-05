from logger import get_logger
import pandas as pd

logger = get_logger()

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply simple transformations to data."""

    logger.info("Starting transformation")

    # Lowercase column names
    df.columns = [col.lower() for col in df.columns]

    # Clean whitespace in string columns
    if "name" in df.columns:
        df["name"] = df["name"].str.strip()

    if "email" in df.columns:
        df["email"] = df["email"].str.strip().str.lower()

    before = len(df)

    # Remove rows with missing email
    if "email" in df.columns:
        df = df[df["email"].notna()]

    after = len(df)

    logger.info(f"Dropped {before - after} rows due to missing email")

    logger.info("Transformation complete")

    return df