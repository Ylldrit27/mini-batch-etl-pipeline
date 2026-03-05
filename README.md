# Simple Batch ETL Pipeline

## Overview
This project demonstrates a small batch ETL (Extract, Transform, Load) pipeline built in Python.

The goal is to simulate a production-style data workflow:
- Extract raw CSV data
- Clean and transform the dataset
- Load the processed data into PostgreSQL
- Run structured queries for analysis

## Concepts Covered
- Batch processing
- Data cleaning & transformation
- Idempotent loading
- Logging
- SQL integration
- Basic data quality checks

## Why This Project?
Built as part of preparation for distributed data engineering and production data systems work.

## Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/Ylldrit27/mini-batch-etl-pipeline.git
cd mini-batch-etl-pipeline

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python src/main.py