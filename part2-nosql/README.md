
---
# Part 2 – NoSQL Database (MongoDB)

## Objective
This part evaluates the suitability of MongoDB for handling FlexiMart’s diverse and evolving product catalog and implements basic MongoDB operations on product data.

---

## Tasks Completed

### 1. NoSQL Justification Report
- Analyzed limitations of relational databases for product catalogs.
- Explained benefits of MongoDB, including:
  - Flexible schema
  - Embedded documents
  - Horizontal scalability
- Identified trade-offs of using MongoDB.

### 2. MongoDB Practical Implementation
- Imported product catalog data into MongoDB.
- Executed queries to:
  - Filter products by category and price
  - Calculate average product ratings
  - Update product reviews
  - Perform aggregation by category

---

## Files in This Folder

- `nosql_analysis.md` – Theory justification report
- `mongodb_operations.js` – MongoDB queries and operations
- `products_catalog.json` – Sample product catalog data

---

## How to Run

```bash
mongosh < mongodb_operations.js
