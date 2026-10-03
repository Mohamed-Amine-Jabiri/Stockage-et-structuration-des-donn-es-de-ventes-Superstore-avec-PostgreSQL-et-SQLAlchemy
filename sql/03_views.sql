-- 03_views.sql
-- Superstore Database - Analytical Views


-- 1. Orders Analysis View

CREATE OR REPLACE VIEW vw_orders_analysis AS
SELECT
    o.order_id,
    o.order_date,
    o.ship_date,
    o.ship_mode,
    o.shipping_days,
    o.shipping_category,

    c.customer_id,
    c.customer_name,
    c.segment,

    c.country,
    c.city,
    c.state,
    c.postal_code,
    c.region

FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id;


-- 2. Sales Analysis View

CREATE OR REPLACE VIEW vw_sales_analysis AS
SELECT
    od.row_id,
    od.order_id,

    o.order_date,
    o.ship_date,
    o.ship_mode,
    o.shipping_days,
    o.shipping_category,

    c.customer_id,
    c.customer_name,
    c.segment,
    c.region,

    p.product_id,
    p.product_name,
    p.category,
    p.sub_category,

    od.sales,
    od.sales_category

FROM order_details od

JOIN orders o
    ON od.order_id = o.order_id

JOIN customers c
    ON o.customer_id = c.customer_id

JOIN products p
    ON od.product_id = p.product_id;