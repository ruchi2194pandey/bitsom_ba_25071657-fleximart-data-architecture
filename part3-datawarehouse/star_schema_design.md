# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

### FACT TABLE: fact_sales
**Grain:** One row per product per order line item  
**Business Process:** Sales transactions

**Measures:**
- quantity_sold: Number of units sold
- unit_price: Price per unit at the time of sale
- discount_amount: Discount applied on the transaction
- total_amount: Final sales amount (quantity × unit_price − discount)

**Foreign Keys:**
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

---

### DIMENSION TABLE: dim_date
**Purpose:** Enables time-based analysis  
**Type:** Conformed dimension  

**Attributes:**
- date_key (PK): Surrogate key (YYYYMMDD)
- full_date: Actual calendar date
- day_of_week: Monday, Tuesday, etc.
- day_of_month: Day number
- month: Month number (1–12)
- month_name: Month name
- quarter: Q1–Q4
- year: Calendar year
- is_weekend: Boolean indicator

---

### DIMENSION TABLE: dim_product
**Purpose:** Product-level analysis  

**Attributes:**
- product_key (PK): Surrogate key
- product_id: Source system product ID
- product_name: Product name
- category: Product category
- subcategory: Product sub-category
- unit_price: Standard product price

---

### DIMENSION TABLE: dim_customer
**Purpose:** Customer profiling and segmentation  

**Attributes:**
- customer_key (PK): Surrogate key
- customer_id: Source customer ID
- customer_name: Full customer name
- city: City
- state: State
- customer_segment: Retail, Corporate, etc.

---

## Section 2: Design Decisions (≈150 words)

The chosen granularity of one row per product per order line item ensures maximum analytical flexibility. This allows detailed analysis such as product-level performance, customer purchase behavior, and time-based trends. Aggregations can be performed easily without losing transactional detail.

Surrogate keys are used instead of natural keys to improve performance and maintain consistency even when source system identifiers change. They also simplify joins and enable efficient indexing.

This star schema design supports drill-down and roll-up operations across multiple dimensions. Analysts can roll up sales data from daily to monthly or yearly levels, or drill down from category-level sales to individual products. The separation of facts and dimensions improves query performance and scalability.

---

## Section 3: Sample Data Flow

**Source Transaction:**  
Order #101, Customer: John Doe, Product: Laptop, Quantity: 2, Price: 50000

**Data Warehouse Representation:**

fact_sales:
