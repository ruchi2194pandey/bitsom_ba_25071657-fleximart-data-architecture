# FlexiMart Database Schema Documentation

## Entity-Relationship Description

### ENTITY: customers
Purpose: Stores customer personal and registration details.

Attributes:
- customer_id: Unique identifier (Primary Key)
- first_name: Customer's first name
- last_name: Customer's last name
- email: Unique email address
- phone: Contact number
- city: Customer city
- registration_date: Date of registration

Relationships:
- One customer can place MANY orders (1:M with orders)

---

### ENTITY: products
Purpose: Stores product catalog information.

Attributes:
- product_id: Unique identifier (Primary Key)
- product_name: Name of product
- category: Product category
- price: Unit price
- stock_quantity: Available inventory

Relationships:
- One product can appear in MANY order_items (1:M)

---

### ENTITY: orders
Purpose: Stores customer purchase transactions.

Attributes:
- order_id: Unique identifier (Primary Key)
- customer_id: References customers.customer_id
- order_date: Date of order
- total_amount: Total order value
- status: Order status

Relationships:
- One order belongs to ONE customer (M:1)
- One order has MANY order_items (1:M)

---

### ENTITY: order_items
Purpose: Stores line-item details of orders.

Attributes:
- order_item_id: Unique identifier (Primary Key)
- order_id: References orders.order_id
- product_id: References products.product_id
- quantity: Units purchased
- unit_price: Price per unit
- subtotal: quantity × unit_price

---

## Normalization Explanation (3NF)

The FlexiMart database is designed following Third Normal Form (3NF) principles. Each table represents a single entity, and all attributes depend solely on the primary key of that table. There are no repeating groups or multi-valued attributes, satisfying First Normal Form (1NF). Second Normal Form (2NF) is achieved because all non-key attributes are fully functionally dependent on the entire primary key; there are no partial dependencies since surrogate keys are used.

Third Normal Form is ensured by eliminating transitive dependencies. For example, customer city information is stored only in the customers table and not duplicated in orders. Product pricing and category details are maintained only in the products table. This separation prevents update anomalies (changing product price in one place), insertion anomalies (adding new products without orders), and deletion anomalies (removing orders without losing product data).

Functional dependencies include:
- customer_id → customer attributes
- product_id → product attributes
- order_id → order attributes
- order_item_id → quantity, price, subtotal

This design ensures data integrity, consistency, and scalability.

---

## Sample Data Representation

### customers
| customer_id | first_name | last_name | email              | city     |
|------------|------------|-----------|-------------------|----------|
| 1          | Rahul      | Sharma    | rahul@gmail.com   | Delhi    |
| 2          | Anita      | Verma     | anita@gmail.com   | Mumbai  |

### products
| product_id | product_name | category     | price |
|-----------|--------------|--------------|-------|
| 1         | Laptop       | Electronics  | 55000 |
| 2         | Headphones   | Electronics  | 3000  |

### orders
| order_id | customer_id | order_date | total_amount |
|---------|-------------|------------|--------------|
| 101     | 1           | 2024-03-15 | 58000        |

### order_items
| order_item_id | order_id | product_id | quantity | subtotal |
|--------------|----------|------------|----------|----------|
| 1            | 101      | 1          | 1        | 55000    |
