import pandas as pd
from sqlalchemy import create_engine

from src.config import DATABASE_URL


CSV_PATH = "data/superstore_clean.csv"


def load_data():
    # Read CSV
    df = pd.read_csv(CSV_PATH)

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Create customers table
    customers = (
        df[
            [
                "Customer ID",
                "Customer Name",
                "Segment",
                "Country",
                "City",
                "State",
                "Postal Code",
                "Region",
            ]
        ]
        .drop_duplicates(subset=["Customer ID"])
        .rename(
            columns={
                "Customer ID": "customer_id",
                "Customer Name": "customer_name",
                "Segment": "segment",
                "Country": "country",
                "City": "city",
                "State": "state",
                "Postal Code": "postal_code",
                "Region": "region",
            }
        )
    )

    # Create products table
    products = (
        df[
            [
                "Product ID",
                "Product Name",
                "Category",
                "Sub-Category",
            ]
        ]
        .drop_duplicates(subset=["Product ID"])
        .rename(
            columns={
                "Product ID": "product_id",
                "Product Name": "product_name",
                "Category": "category",
                "Sub-Category": "sub_category",
            }
        )
    )

    # Create orders table
    orders = (
        df[
            [
                "Order ID",
                "Customer ID",
                "Order Date",
                "Ship Date",
                "Ship Mode",
                "Shipping Days",
                "Shipping Category",
            ]
        ]
        .drop_duplicates(subset=["Order ID"])
        .rename(
            columns={
                "Order ID": "order_id",
                "Customer ID": "customer_id",
                "Order Date": "order_date",
                "Ship Date": "ship_date",
                "Ship Mode": "ship_mode",
                "Shipping Days": "shipping_days",
                "Shipping Category": "shipping_category",
            }
        )
    )

    # Create order_details table
    order_details = (
        df[
            [
                "Row ID",
                "Order ID",
                "Product ID",
                "Sales",
                "sales category",
            ]
        ]
        .rename(
            columns={
                "Row ID": "row_id",
                "Order ID": "order_id",
                "Product ID": "product_id",
                "Sales": "sales",
                "sales category": "sales_category",
            }
        )
    )

    # Connect to PostgreSQL
    engine = create_engine(DATABASE_URL)

    # Load data into PostgreSQL
    customers.to_sql(
        "customers",
        engine,
        if_exists="append",
        index=False,
    )

    products.to_sql(
        "products",
        engine,
        if_exists="append",
        index=False,
    )

    orders.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False,
    )

    order_details.to_sql(
        "order_details",
        engine,
        if_exists="append",
        index=False,
    )

    print("Data loaded successfully!")
    print(f"Customers: {len(customers)}")
    print(f"Products: {len(products)}")
    print(f"Orders: {len(orders)}")
    print(f"Order details: {len(order_details)}")


if __name__ == "__main__":
    load_data()