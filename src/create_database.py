import psycopg2
from psycopg2 import sql

from src.config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


def create_database():
    """Create the Superstore database if it does not already exist."""

    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
        )

        connection.autocommit = True

        cursor = connection.cursor()

        # Check if database already exists
        cursor.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s",
            (DB_NAME,)
        )

        exists = cursor.fetchone()

        if exists:
            print(f"Database '{DB_NAME}' already exists.")

        else:
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(DB_NAME)
                )
            )

            print(f"Database '{DB_NAME}' created successfully.")

    except Exception as e:
        print(f"Database creation error: {e}")
        raise

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    create_database()