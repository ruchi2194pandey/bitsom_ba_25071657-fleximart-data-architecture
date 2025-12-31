USE fleximart_dw;

-- dim_date (Jan–Feb 2024, 30 dates)
INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,0),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,1),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,0),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,1),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,0),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,1);

-- dim_product (15 products)
INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Laptop Pro','Electronics','Computers',50000),
('P002','Smartphone X','Electronics','Mobile',30000),
('P003','LED TV','Electronics','TV',45000),
('P004','Office Chair','Furniture','Seating',8000),
('P005','Dining Table','Furniture','Table',25000),
('P006','T-Shirt','Clothing','Topwear',999),
('P007','Jeans','Clothing','Bottomwear',1999),
('P008','Jacket','Clothing','Winter',4999),
('P009','Mixer Grinder','Appliances','Kitchen',7000),
('P010','Washing Machine','Appliances','Laundry',32000),
('P011','Refrigerator','Appliances','Cooling',42000),
('P012','Shoes','Clothing','Footwear',2999),
('P013','Headphones','Electronics','Audio',5999),
('P014','Smart Watch','Electronics','Wearable',12000),
('P015','Sofa','Furniture','Living',55000);

-- dim_customer (12 customers)
INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','John Doe','Mumbai','MH','Retail'),
('C002','Anita Sharma','Delhi','DL','Corporate'),
('C003','Rahul Verma','Bangalore','KA','Retail'),
('C004','Sneha Iyer','Chennai','TN','Retail'),
('C005','Amit Patel','Ahmedabad','GJ','Corporate'),
('C006','Neha Singh','Pune','MH','Retail'),
('C007','Rohit Mehta','Jaipur','RJ','Retail'),
('C008','Kavya Rao','Hyderabad','TS','Corporate'),
('C009','Suresh Kumar','Coimbatore','TN','Retail'),
('C010','Pooja Nair','Kochi','KL','Retail'),
('C011','Vikas Jain','Indore','MP','Retail'),
('C012','Manish Gupta','Noida','UP','Corporate');

-- fact_sales (40+ records – sample)
INSERT INTO fact_sales (date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount) VALUES
(20240115,1,1,2,50000,0,100000),
(20240120,2,2,1,30000,2000,28000),
(20240201,3,3,1,45000,0,45000),
(20240210,6,4,3,999,0,2997),
(20240210,7,5,2,1999,0,3998),
(20240106,4,6,1,8000,500,7500),
(20240115,5,7,1,25000,0,25000),
(20240120,8,8,1,4999,0,4999),
(20240201,9,9,2,7000,0,14000),
(20240210,10,10,1,32000,2000,30000);
