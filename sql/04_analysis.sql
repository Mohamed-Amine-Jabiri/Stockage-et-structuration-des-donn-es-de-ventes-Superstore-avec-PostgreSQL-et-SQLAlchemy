-- 04_analysis.sql
-- Superstore Database - Analysis Queries


-- 1. TOTAL SALES

SELECT
    SUM(sales) AS total_sales
FROM order_details;


-- 2. NUMBER OF ORDERS

SELECT
    COUNT(*) AS total_orders
FROM orders;


-- 3. NUMBER OF CUSTOMERS

SELECT
    COUNT(*) AS total_customers
FROM customers;


-- 4. NUMBER OF PRODUCTS

SELECT
    COUNT(*) AS total_products
FROM products;


-- 5. SALES BY CATEGORY

SELECT
    category,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY category
ORDER BY total_sales DESC;


-- 6. SALES BY SUB-CATEGORY

SELECT
    sub_category,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY sub_category
ORDER BY total_sales DESC;


-- 7. SALES BY REGION

SELECT
    region,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY region
ORDER BY total_sales DESC;


-- 8. SALES BY CUSTOMER SEGMENT

SELECT
    segment,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY segment
ORDER BY total_sales DESC;


-- 9. TOP 10 CUSTOMERS BY SALES

SELECT
    customer_id,
    customer_name,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY
    customer_id,
    customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- 10. TOP 10 PRODUCTS BY SALES

SELECT
    product_id,
    product_name,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY
    product_id,
    product_name
ORDER BY total_sales DESC
LIMIT 10;


-- 11. SALES BY YEAR

SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY year
ORDER BY year;


-- 12. SALES BY MONTH

SELECT
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date)
ORDER BY
    year,
    month;


-- 13. ORDERS BY SHIPPING MODE

SELECT
    ship_mode,
    COUNT(*) AS total_orders
FROM orders
GROUP BY ship_mode
ORDER BY total_orders DESC;


-- 14. AVERAGE SHIPPING DAYS

SELECT
    AVG(shipping_days) AS average_shipping_days
FROM orders;


-- 15. SALES BY SHIPPING CATEGORY

SELECT
    shipping_category,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY shipping_category
ORDER BY total_sales DESC;


-- 16. AVERAGE SALES PER ORDER

SELECT
    AVG(order_total) AS average_order_value
FROM (
    SELECT
        order_id,
        SUM(sales) AS order_total
    FROM order_details
    GROUP BY order_id
) AS order_totals;


-- 17. TOP 10 ORDERS BY SALES

SELECT
    order_id,
    SUM(sales) AS total_sales
FROM order_details
GROUP BY order_id
ORDER BY total_sales DESC
LIMIT 10;


-- 18. PRODUCTS COUNT BY CATEGORY

SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;


-- 19. SALES BY CITY

SELECT
    city,
    SUM(sales) AS total_sales
FROM vw_sales_analysis
GROUP BY city
ORDER BY total_sales DESC
LIMIT 10;


-- 20. COMPLETE SALES KPI

SELECT
    SUM(sales) AS total_sales,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT product_id) AS total_products,
    AVG(sales) AS average_line_sales
FROM vw_sales_analysis;