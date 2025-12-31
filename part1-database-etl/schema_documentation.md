# FlexiMart Database Schema Documentation

## 1. Entity Relationship Overview

The FlexiMart transactional database consists of four core entities:

- Customers
- Products
- Orders
- Order_Items

A customer can place multiple orders (one-to-many).  
Each order can contain multiple products, resolved using the Order_Items table (many-to-many).

---

## 2. Table Descriptions

### Customers
| Column | Description |
|------|------------|
| customer_id (PK) | Unique customer identifier |
| first_name | Customer first name |
| last_name | Customer last name |
| email | Unique email address |
| phone | Standardized phone number |
| city | Customer city |
| registration_date | Date of registration |

---

### Products
| Column | Description |
|------|------------|
| product_id (PK) | Unique product identifier |
| product_name | Name of the product |
| category | Product category |
| price | Unit price |
| stock_quantity | Available stock |

---

### Orders
| Column | Description |
|------|------------|
| order_id (PK) | Unique order identifier |
| customer_id (FK) | Reference to customers |
| order_date | Date of order |
| total_amount | Total order value |

---

### Order_Items
| Column | Description |
|------|------------|
| order_item_id (PK) | Unique row identifier |
| order_id (FK) | Reference to orders |
| product_id (FK) | Reference to products |
| quantity | Quantity purchased |
| unit_price | Price per unit |
| subtotal | quantity × unit_price |

---

## 3. Normalization (3NF Explanation)

The schema follows Third Normal Form (3NF). Each table contains atomic attributes, ensuring First Normal Form (1NF). Partial dependencies are removed by separating order and product details into the Order_Items table, satisfying Second Normal Form (2NF). There are no transitive dependencies; non-key attributes depend only on the primary key of their respective tables. For example, customer contact information is stored only in the Customers table and not duplicated in Orders. This structure reduces redundancy, improves data integrity, and ensures efficient updates, making the database scalable and maintainable.

---

## 4. Sample Records

### Customers
| customer_id | first_name | last_name | email |
|------------|-----------|-----------|-------|
| 1 | Rahul | Sharma | rahul@gmail.com |

### Products
| product_id | product_name | category | price |
|-----------|-------------|----------|-------|
| 101 | iPhone 14 | Electronics | 69999 |

### Orders
| order_id | customer_id | total_amount |
|---------|-------------|--------------|
| 9001 | 1 | 69999 |

### Order_Items
| order_item_id | order_id | product_id | quantity |
|--------------|----------|------------|----------|
| 1 | 9001 | 101 | 1 |
