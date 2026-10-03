# Superstore Database Schema

## 1. Project Overview

This project transforms the Superstore sales dataset into a normalized PostgreSQL database.

The database is structured into four main tables:

* `customers`
* `products`
* `orders`
* `order_details`

The objective is to reduce data redundancy, improve data integrity, and facilitate SQL analysis.

---

## 2. Database Architecture

```text
                    ┌──────────────────┐
                    │    customers     │
                    ├──────────────────┤
                    │ PK customer_id   │
                    │ customer_name    │
                    │ segment          │
                    │ country          │
                    │ city             │
                    │ state            │
                    │ postal_code      │
                    │ region           │
                    └────────┬─────────┘
                             │
                             │ 1
                             │
                             │ N
                    ┌────────▼─────────┐
                    │      orders      │
                    ├──────────────────┤
                    │ PK order_id      │
                    │ FK customer_id   │
                    │ order_date      │
                    │ ship_date       │
                    │ ship_mode       │
                    │ shipping_days   │
                    │ shipping_category│
                    └────────┬─────────┘
                             │
                             │ 1
                             │
                             │ N
                  ┌──────────▼──────────┐
                  │   order_details     │
                  ├─────────────────────┤
                  │ PK row_id           │
                  │ FK order_id         │
                  │ FK product_id       │
                  │ sales               │
                  │ sales_category     │
                  └──────────┬──────────┘
                             │
                             │ N
                             │
                             │ 1
                    ┌────────▼─────────┐
                    │     products     │
                    ├──────────────────┤
                    │ PK product_id   │
                    │ product_name    │
                    │ category        │
                    │ sub_category    │
                    └──────────────────┘
```

---

## 3. Tables

### 3.1 Customers

The `customers` table contains unique customer information.

| Column          | Type         | Constraint | Description                |
| --------------- | ------------ | ---------- | -------------------------- |
| `customer_id`   | VARCHAR(20)  | PK         | Unique customer identifier |
| `customer_name` | VARCHAR(100) | NOT NULL   | Customer name              |
| `segment`       | VARCHAR(50)  | NOT NULL   | Customer segment           |
| `country`       | VARCHAR(100) |            | Country                    |
| `city`          | VARCHAR(100) |            | City                       |
| `state`         | VARCHAR(100) |            | State                      |
| `postal_code`   | INTEGER      |            | Postal code                |
| `region`        | VARCHAR(50)  |            | Geographic region          |

**Primary Key:** `customer_id`

---

### 3.2 Products

The `products` table contains unique products.

| Column         | Type        | Constraint | Description               |
| -------------- | ----------- | ---------- | ------------------------- |
| `product_id`   | VARCHAR(30) | PK         | Unique product identifier |
| `product_name` | TEXT        | NOT NULL   | Product name              |
| `category`     | VARCHAR(50) | NOT NULL   | Product category          |
| `sub_category` | VARCHAR(50) | NOT NULL   | Product sub-category      |

**Primary Key:** `product_id`

---

### 3.3 Orders

The `orders` table contains information about customer orders.

One customer can have multiple orders.

| Column              | Type        | Constraint   | Description                   |
| ------------------- | ----------- | ------------ | ----------------------------- |
| `order_id`          | VARCHAR(30) | PK           | Unique order identifier       |
| `customer_id`       | VARCHAR(20) | FK, NOT NULL | Customer who placed the order |
| `order_date`        | DATE        | NOT NULL     | Date of the order             |
| `ship_date`         | DATE        | NOT NULL     | Shipping date                 |
| `ship_mode`         | VARCHAR(50) | NOT NULL     | Shipping method               |
| `shipping_days`     | INTEGER     |              | Number of shipping days       |
| `shipping_category` | VARCHAR(50) |              | Shipping category             |

**Primary Key:** `order_id`

**Foreign Key:**

```text
customer_id → customers.customer_id
```

---

### 3.4 Order Details

The `order_details` table contains the products included in each order.

An order can contain multiple products.

| Column           | Type          | Constraint   | Description            |
| ---------------- | ------------- | ------------ | ---------------------- |
| `row_id`         | INTEGER       | PK           | Unique line identifier |
| `order_id`       | VARCHAR(30)   | FK, NOT NULL | Related order          |
| `product_id`     | VARCHAR(30)   | FK, NOT NULL | Related product        |
| `sales`          | NUMERIC(12,2) | NOT NULL     | Sales amount           |
| `sales_category` | VARCHAR(50)   |              | Sales category         |

**Primary Key:** `row_id`

**Foreign Keys:**

```text
order_id → orders.order_id
product_id → products.product_id
```

---

## 4. Relationships

### Customers → Orders

Relationship:

```text
customers 1 ─────── N orders
```

A customer can have multiple orders.

Each order belongs to one customer.

---

### Orders → Order Details

Relationship:

```text
orders 1 ─────── N order_details
```

An order can contain multiple order detail lines.

Each order detail belongs to one order.

---

### Products → Order Details

Relationship:

```text
products 1 ─────── N order_details
```

A product can appear in multiple order details.

Each order detail references one product.

---

## 5. Foreign Key Constraints

The database contains three main foreign key relationships.

### Orders → Customers

```sql
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);
```

### Order Details → Orders

```sql
ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);
```

### Order Details → Products

```sql
ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);
```

---

## 6. Normalization

The database is organized to reduce data duplication.

### Before normalization

The original dataset contains customer, product, order, and sales information in the same table.

For example, the same customer information can appear on multiple rows.

```text
Order ID
Customer ID
Customer Name
City
Region
Product ID
Product Name
Category
Sales
...
```

This creates repeated information.

### After normalization

The information is
