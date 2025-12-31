# Part 1 – Database Design and ETL Pipeline

## Objective
This part focuses on building an end-to-end ETL pipeline to ingest raw CSV data into a relational database (MySQL), handle data quality issues, document the database schema, and answer business questions using SQL.

---

## Tasks Completed

### 1. ETL Pipeline Implementation
- Extracted data from three raw CSV files:
  - customers_raw.csv
  - products_raw.csv
  - sales_raw.csv
- Cleaned and transformed data by:
  - Removing duplicate records
  - Handling missing values appropriately (drop or default)
  - Standardizing phone numbers and category names
  - Converting dates to YYYY-MM-DD format
- Loaded cleaned data into MySQL tables using Python.

### 2. Database Schema Documentation
- Documented entities, attributes, and relationships.
- Explained normalization and justified 3NF compliance.
- Provided sample data representations for each table.

### 3. Business Query Implementation
- Wrote SQL queries to answer:
  - Customer purchase history
  - Product sales analysis
  - Monthly sales trends

---

## Files in This Folder

- `etl_pipeline.py` – Python ETL script
- `schema_documentation.md` – Database design and normalization explanation
- `business_queries.sql` – SQL queries for business scenarios
- `data_quality_report.txt` – Summary of data cleaning results
- `requirements.txt` – Python dependencies

---

## How to Run

```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"
python etl_pipeline.py
mysql -u root -p fleximart < business_queries.sql
