"""
ETL Pipeline for FlexiMart
Author: Ruchi Harishanker Pandey
"""

import pandas as pd
import re
import logging
from sqlalchemy import create_engine

# ---------------- CONFIG ---------------- #
DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_NAME = "fleximart"

CUSTOMERS_CSV = "customers_raw.csv"
PRODUCTS_CSV = "product_raw.csv"
SALES_CSV = "sales_raw.csv"

REPORT_FILE = "data_quality_report.txt"

# ---------------- LOGGING ---------------- #
logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- HELPERS ---------------- #
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))
    return f"+91-{digits[-10:]}" if len(digits) >= 10 else None

def standardize_category(cat):
    if pd.isna(cat):
        return "Unknown"
    return cat.strip().title()

# ---------------- EXTRACT ---------------- #
customers = pd.read_csv(CUSTOMERS_CSV)
products = pd.read_csv(PRODUCTS_CSV)
sales = pd.read_csv(SALES_CSV)

# Normalize column names everywhere
customers.columns = customers.columns.str.strip().str.lower()
products.columns = products.columns.str.strip().str.lower()
sales.columns = sales.columns.str.strip().str.lower()

report = []

# ---------------- TRANSFORM ---------------- #
# Remove duplicates
cust_dupes = customers.duplicated().sum()
prod_dupes = products.duplicated().sum()
sales_dupes = sales.duplicated().sum()

customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)

# -------- Customers --------
customers["city"] = customers["city"].fillna("Unknown")
customers["phone"] = customers["phone"].apply(standardize_phone)

customers["registration_date"] = pd.to_datetime(
    customers["registration_date"],
    errors="coerce",
    dayfirst=True
).dt.strftime("%Y-%m-%d")

# -------- Products --------
# stock_quantity fix
if "stock_quantity" not in products.columns:
    if "stock_qty" in products.columns:
        products.rename(columns={"stock_qty": "stock_quantity"}, inplace=True)
    elif "quantity" in products.columns:
        products.rename(columns={"quantity": "stock_quantity"}, inplace=True)
    else:
        products["stock_quantity"] = 0

products["stock_quantity"] = products["stock_quantity"].fillna(0).astype(int)

# category fix
if "category" not in products.columns:
    if "product_category" in products.columns:
        products.rename(columns={"product_category": "category"}, inplace=True)
    else:
        products["category"] = "Unknown"

products["category"] = products["category"].apply(standardize_category)

# -------- Sales --------
# Rename sales columns safely
sales_column_map = {
    "orderdate": "order_date",
    "date": "order_date",
    "amount": "total_amount",
    "total": "total_amount",
    "cust_id": "customer_id"
}

for old, new in sales_column_map.items():
    if old in sales.columns and new not in sales.columns:
        sales.rename(columns={old: new}, inplace=True)

# Drop NA only for columns that exist
critical_cols = [c for c in ["order_date", "customer_id", "total_amount"] if c in sales.columns]
sales.dropna(subset=critical_cols, inplace=True)

# Standardize order_date if present
if "order_date" in sales.columns:
    sales["order_date"] = pd.to_datetime(
        sales["order_date"],
        errors="coerce",
        dayfirst=True
    ).dt.strftime("%Y-%m-%d")

# ---------------- LOAD ---------------- #
engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

customers.to_sql("customers", engine, if_exists="append", index=False)
products.to_sql("products", engine, if_exists="append", index=False)
sales.to_sql("orders", engine, if_exists="append", index=False)

# ---------------- REPORT ---------------- #
report.extend([
    f"Customer duplicates removed: {cust_dupes}",
    f"Product duplicates removed: {prod_dupes}",
    f"Sales duplicates removed: {sales_dupes}",
    f"Customers loaded: {len(customers)}",
    f"Products loaded: {len(products)}",
    f"Orders loaded: {len(sales)}"
])

with open(REPORT_FILE, "w") as f:
    f.write("\n".join(report))

print("✅ ETL completed successfully")
