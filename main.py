from src.create_database import create_database
from src.test_connection import test_connection
from src.load_data import load_data
from src.database import execute_sql_file

import pytest


def main():

    print("\n")
    print("=" * 60)
    print("SUPERSTORE DATA PROJECT")
    print("=" * 60)

    try:
        # 1. Create database
        print("\n[1/8] Creating database...")
        create_database()

        # 2. Test PostgreSQL connection
        print("\n[2/8] Testing PostgreSQL connection...")
        if not test_connection():
            print("\nDatabase connection failed.")
            return

        # 3. Create tables
        print("\n[3/8] Creating tables...")
        execute_sql_file("sql/01_create_tables.sql")

        # 4. Load data
        print("\n[4/8] Loading Superstore data...")
        load_data()

        # 5. Add constraints
        print("\n[5/8] Adding primary keys and foreign keys...")
        execute_sql_file("sql/02_constraints.sql")

        # 6. Run integrity tests
        print("\n[6/8] Running integrity tests...")

        result = pytest.main([
            "tests/test_integrity.py",
            "-v"
        ])

        if result != 0:
            print("\nIntegrity tests failed.")
            return

        # 7. Create analytical views
        print("\n[7/8] Creating analytical views...")
        execute_sql_file("sql/03_views.sql")

        # 8. Run analysis
        print("\n[8/8] Running SQL analysis...")
        execute_sql_file("sql/04_analysis.sql")

        print("\n")
        print("=" * 60)
        print("PROJECT EXECUTED SUCCESSFULLY")
        print("=" * 60)

    except Exception as e:

        print("\n")
        print("=" * 60)
        print("PROJECT FAILED")
        print("=" * 60)

        print(f"\nError: {e}")


if __name__ == "__main__":
    main()