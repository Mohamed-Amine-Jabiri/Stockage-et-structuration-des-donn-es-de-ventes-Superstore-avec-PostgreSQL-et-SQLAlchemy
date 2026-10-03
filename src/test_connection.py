from sqlalchemy import text

from src.database import engine


def test_connection():
    """Test the PostgreSQL database connection."""

    try:
        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT version();")
            )

            version = result.fetchone()[0]

            print("Connection successful!")
            print("PostgreSQL version:")
            print(version)

            return True

    except Exception as e:

        print("Connection failed!")
        print(f"Error: {e}")

        return False


if __name__ == "__main__":
    test_connection()