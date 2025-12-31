import pandas as pd
import mysql.connector
from datetime import datetime

# -------------------------------
# DATABASE CONNECTION
# -------------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="fleximart"
)
cursor = conn.cursor()

# -------------------------------
# DATA QUALITY METRICS
# -------------------------------
report = []

# -------------------------------
# CUSTOMERS ETL
# -------------------------------
customers = pd.read_csv("../data/customers_raw.csv")

initial_count = len(customers)

# Drop missing emails
customers = customers.dropna(subset=["email"])

# Remove duplicates
customers = customers.drop_duplicates(subset=["first_name", "last_name", "email"])

# Standardize phone numbers
def clean_phone(phone):
    try:
        phone = str(int(float(phone)))
        return "+91-" + phone[-10:]
    except:
        return None

customers["phone"] = customers["phone"].apply(clean_phone)

# Convert registration date
customers["registration_date"] = pd.to_datetime(
    customers["registration_date"], errors="coerce"
).dt.date

customer_loaded = len(customers)

report.append(f"""
File: customers_raw.csv
Total records read           : {initial_count}
Records loaded successfully  : {customer_loaded}
""")

# Load customers
for _, row in customers.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO customers
        (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

# -------------------------------
# PRODUCTS ETL
# -------------------------------
products_raw = pd.read_csv("../data/products_raw.csv", header=None)
products = products_raw[0].str.split(",", expand=True)
products.columns = ["product_id", "product_name", "category", "price", "stock_quantity"]

products["price"] = pd.to_numeric(products["price"], errors="coerce")
products = products.dropna(subset=["price"])

products["stock_quantity"] = pd.to_numeric(
    products["stock_quantity"], errors="coerce"
).fillna(0)

products["category"] = products["category"].str.strip().str.title()

product_loaded = len(products)

report.append(f"""
File: products_raw.csv
Records loaded successfully  : {product_loaded}
""")

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products
        (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """, (row["product_name"], row["category"], row["price"], row["stock_quantity"]))

conn.commit()

# -------------------------------
# SALES ETL
# -------------------------------
sales = pd.read_csv("../data/sales_raw.csv")

initial_sales = len(sales)

sales = sales.dropna(subset=["customer_id", "product_id"])
sales = sales.drop_duplicates()

sales["order_date"] = pd.to_datetime(
    sales["order_date"], errors="coerce", dayfirst=True
).dt.date

sales_loaded = len(sales)

report.append(f"""
File: sales_raw.csv
Records loaded successfully  : {sales_loaded}
""")

for _, row in sales.iterrows():
    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount)
        VALUES (%s, %s, %s)
    """, (row["customer_id"], row["order_date"], row["total_amount"]))

conn.commit()

# -------------------------------
# WRITE DATA QUALITY REPORT
# -------------------------------
with open("data_quality_report.txt", "w") as f:
    f.write("FlexiMart Data Quality Report\n")
    f.write("=============================\n")
    for r in report:
        f.write(r)

cursor.close()
conn.close()

print("ETL Pipeline executed successfully.")
