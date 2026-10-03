import pandas as pd


def transform_data(df):
    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Convert numeric columns
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Shipping Days"] = pd.to_numeric(
        df["Shipping Days"],
        errors="coerce"
    )

    # Remove rows with missing critical identifiers
    df = df.dropna(
        subset=[
            "Row ID",
            "Order ID",
            "Customer ID",
            "Product ID",
        ]
    )

    # Remove duplicate Row IDs
    df = df.drop_duplicates(subset=["Row ID"])

    return df


def validate_data(df):
    # Check duplicated Row IDs
    duplicate_rows = df["Row ID"].duplicated().sum()

    # Check missing values
    missing_values = df.isnull().sum().sum()

    # Check negative sales
    negative_sales = (df["Sales"] < 0).sum()

    print("Data validation")
    print("----------------")
    print(f"Rows: {len(df)}")
    print(f"Duplicate Row IDs: {duplicate_rows}")
    print(f"Missing values: {missing_values}")
    print(f"Negative sales: {negative_sales}")

    return (
        duplicate_rows == 0
        and missing_values == 0
        and negative_sales == 0
    )


if __name__ == "__main__":
    df = pd.read_csv("data/superstore_clean.csv")

    df = transform_data(df)

    is_valid = validate_data(df)

    if is_valid:
        print("Data is valid.")
    else:
        print("Data validation failed.")