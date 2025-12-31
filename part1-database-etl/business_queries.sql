/* -------------------------------------------
Query 1:
Top 5 customers by total spending
-------------------------------------------- */
SELECT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, customer_name
ORDER BY total_spent DESC
LIMIT 5;


/* -------------------------------------------
Query 2:
Monthly sales trend (total revenue per month)
-------------------------------------------- */
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS monthly_revenue
FROM orders
GROUP BY month
ORDER BY month;


/* -------------------------------------------
Query 3:
Products with sales above category average
(Using window function)
-------------------------------------------- */
SELECT
    product_id,
    product_name,
    category,
    total_sales
FROM (
    SELECT
        p.product_id,
        p.product_name,
        p.category,
        SUM(oi.subtotal) AS total_sales,
        AVG(SUM(oi.subtotal)) OVER (PARTITION BY p.category) AS category_avg
    FROM products p
    JOIN order_items oi ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name, p.category
) t
WHERE total_sales > category_avg;
