# Simple Batch ETL Pipeline

## Overview
This project demonstrates a simple batch ETL (Extract, Transform, Load) pipeline built in Python to simulate a real-world data ingestion and processing workflow.

The goal is to simulate a production-style data workflow:
- Extract raw CSV data
- Clean and transform the dataset
- Load the processed data into SQLite
- Run structured queries for analysis

## Concepts Covered
- Batch processing
- Data cleaning & transformation
- Idempotent data loading
- Structured logging
- Error handling
- SQL integration
- Basic data quality checks

## Pipeline Architecture

The pipeline follows a simple batch ETL structure:

Raw CSV → Extract → Transform → Data Quality Checks → Load into SQLite (idempotent) → SQL Queries

The pipeline is designed to separate extraction, transformation, and loading logic into modular components to improve maintainability and readability.

## Project Structure

```
mini-batch-etl-pipeline/
│
├── data/
│   └── raw_customers.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── query.py
│   ├── run_queries.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

Note: `venv/` is ignored in `.gitignore`; create your own virtual environment.

## Why This Project?
Built as part of preparation for distributed data engineering and production data systems work. Demonstrates core ETL concepts, modular pipeline design, logging, idempotency, and SQL integration — all essential skills for real-world data engineering roles.

## Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/Ylldrit27/mini-batch-etl-pipeline.git
cd mini-batch-etl-pipeline

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python src/main.py