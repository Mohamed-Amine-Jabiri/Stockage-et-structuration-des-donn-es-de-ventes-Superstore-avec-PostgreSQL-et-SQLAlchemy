from sqlalchemy import create_engine, text

from src.config import DATABASE_URL


engine = create_engine(DATABASE_URL)


def test_customer_ids_unique():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT customer_id, COUNT(*)
                FROM customers
                GROUP BY customer_id
                HAVING COUNT(*) > 1;
            """)
        )

        duplicates = result.fetchall()

        assert len(duplicates) == 0


def test_product_ids_unique():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT product_id, COUNT(*)
                FROM products
                GROUP BY product_id
                HAVING COUNT(*) > 1;
            """)
        )

        duplicates = result.fetchall()

        assert len(duplicates) == 0


def test_order_ids_unique():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT order_id, COUNT(*)
                FROM orders
                GROUP BY order_id
                HAVING COUNT(*) > 1;
            """)
        )

        duplicates = result.fetchall()

        assert len(duplicates) == 0


def test_row_ids_unique():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT row_id, COUNT(*)
                FROM order_details
                GROUP BY row_id
                HAVING COUNT(*) > 1;
            """)
        )

        duplicates = result.fetchall()

        assert len(duplicates) == 0


def test_orders_have_customers():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT o.order_id
                FROM orders o
                LEFT JOIN customers c
                    ON o.customer_id = c.customer_id
                WHERE c.customer_id IS NULL;
            """)
        )

        invalid_orders = result.fetchall()

        assert len(invalid_orders) == 0


def test_order_details_have_orders():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT od.row_id
                FROM order_details od
                LEFT JOIN orders o
                    ON od.order_id = o.order_id
                WHERE o.order_id IS NULL;
            """)
        )

        invalid_details = result.fetchall()

        assert len(invalid_details) == 0


def test_order_details_have_products():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT od.row_id
                FROM order_details od
                LEFT JOIN products p
                    ON od.product_id = p.product_id
                WHERE p.product_id IS NULL;
            """)
        )

        invalid_details = result.fetchall()

        assert len(invalid_details) == 0


def test_sales_not_negative():
    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT COUNT(*)
                FROM order_details
                WHERE sales < 0;
            """)
        )

        negative_sales = result.scalar()

        assert negative_sales == 0