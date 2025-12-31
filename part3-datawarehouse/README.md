
---
# Part 3 – Data Warehouse and Analytics

## Objective
This part focuses on designing and implementing a data warehouse using a star schema and generating OLAP analytics to support strategic decision-making at FlexiMart.

---

## Tasks Completed

### 1. Star Schema Design
- Designed a star schema with:
  - One fact table (`fact_sales`)
  - Three dimension tables (`dim_date`, `dim_product`, `dim_customer`)
- Documented schema design, granularity, and data flow.

### 2. Data Warehouse Implementation
- Created dimension and fact tables in MySQL.
- Loaded realistic sample data following business rules and constraints.

### 3. OLAP Analytics Queries
- Implemented analytical queries for:
  - Time-based drill-down analysis
  - Top product performance
  - Customer value segmentation

---

## Files in This Folder

- `star_schema_design.md` – Star schema documentation
- `warehouse_schema.sql` – Data warehouse schema creation
- `warehouse_data.sql` – Data population scripts
- `analytics_queries.sql` – OLAP analytical queries

---

## How to Run

```bash
mysql -u root -p fleximart_dw < warehouse_schema.sql
mysql -u root -p fleximart_dw < warehouse_data.sql
mysql -u root -p fleximart_dw < analytics_queries.sql
