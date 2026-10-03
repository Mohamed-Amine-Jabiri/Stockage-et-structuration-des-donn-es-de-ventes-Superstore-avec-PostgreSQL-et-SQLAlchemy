-- 01_create_tables.sql
-- Superstore Database - Table Creation


-- 1. CUSTOMERS

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    segment VARCHAR(50) NOT NULL,
    country VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code INTEGER,
    region VARCHAR(50)
);


-- 2. PRODUCTS

CREATE TABLE products (
    product_id VARCHAR(30) PRIMARY KEY,
    product_name TEXT NOT NULL,
    category VARCHAR(50) NOT NULL,
    sub_category VARCHAR(50) NOT NULL
);


-- 3. ORDERS

CREATE TABLE orders (
    order_id VARCHAR(30) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    order_date DATE NOT NULL,
    ship_date DATE NOT NULL,
    ship_mode VARCHAR(50) NOT NULL,
    shipping_days INTEGER,
    shipping_category VARCHAR(50)
);



-- 4. ORDER_DETAILS

CREATE TABLE order_details (
    row_id INTEGER PRIMARY KEY,
    order_id VARCHAR(30) NOT NULL,
    product_id VARCHAR(30) NOT NULL,
    sales NUMERIC(12, 2) NOT NULL,
    sales_category VARCHAR(50)
);