from extract import extract_data
from transform import transform_data
from load import load_data
from logger import get_logger

logger = get_logger()

def run_pipeline():
    """Main ETL pipeline orchestration."""

    logger.info("===== STARTING ETL PIPELINE =====")

    try:
        # Extract
        logger.info("Step 1: Extract")
        raw_data = extract_data()

        # Transform
        logger.info("Step 2: Transform")
        clean_data = transform_data(raw_data)

        # Load (idempotent)
        logger.info("Step 3: Load")
        load_data(clean_data)

        logger.info("===== PIPELINE COMPLETED SUCCESSFULLY =====")

    except Exception as e:
        logger.error("Pipeline failed!", exc_info=True)
        raise e

if __name__ == "__main__":
    run_pipeline()