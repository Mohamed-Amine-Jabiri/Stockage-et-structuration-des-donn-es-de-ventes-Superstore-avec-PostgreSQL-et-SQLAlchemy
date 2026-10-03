-- 02_constraints.sql
-- Superstore Database - Constraints & Relationships


-- 1. ORDERS → CUSTOMERS

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);



-- 2. ORDER_DETAILS → ORDERS

ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);


-- 3. ORDER_DETAILS → PRODUCTS

ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);