# FlexiMart Data Architecture Project

**Student Name:** Ruchi Harishanker Pandey
**Student ID:** bitsom_ba_25071657
**Email:** ruchi2194.pandey@gmail.com  
**Course:** Data for Artificial Intelligence  
**Module:** AI Data Architecture Design and Implementation  
**Date:** 08 Jan 2026

---

## Project Overview

This project implements an end-to-end data architecture for FlexiMart, an e-commerce company. It includes an ETL pipeline to clean and load raw CSV data into a relational database, NoSQL analysis using MongoDB, and a data warehouse designed with a star schema to support advanced analytics and reporting.

---

## Repository Structure
bitsom_ba_25071657-fleximart-data-architecture/
│
├── README.md
├── .gitignore
│
├── data/
│ ├── customers_raw.csv
│ ├── products_raw.csv
│ └── sales_raw.csv
│
├── part1-database-etl/
│ ├── README.md
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ ├── data_quality_report.txt
│ └── requirements.txt
│
├── part2-nosql/
│ ├── README.md
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
│
└── part3-datawarehouse/
├── README.md
├── star_schema_design.md
├── warehouse_schema.sql
├── warehouse_data.sql
└── analytics_queries.sql


---

## Technologies Used

- **Python 3.x** (pandas, mysql-connector-python)
- **MySQL 8.0**
- **MongoDB 6.0**
- **Git & GitHub**

---

## Setup Instructions

### Relational Database Setup (Part 1)

```bash
mysql -u root -p -e "CREATE DATABASE fleximart;"
python part1-database-etl/etl_pipeline.py
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

## MongoDB Setup (Part 2)
mongosh < part2-nosql/mongodb_operations.js

## Data Warehouse Setup (Part 3)
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

## Key Learnings
Designed and implemented a complete ETL pipeline with data quality handling
Gained hands-on experience with relational, NoSQL, and data warehouse modeling
Learned dimensional modeling and OLAP query design
Improved understanding of scalable data architecture for AI systems

# Challenges Faced
Handling inconsistent and missing data across multiple CSV files – solved using pandas transformations.
Designing a star schema that balances granularity and performance.
Writing efficient aggregation and window-function-based SQL queries.