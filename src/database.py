from pathlib import Path

from sqlalchemy import create_engine, text

from src.config import DATABASE_URL


# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


def get_engine():
    """
    Return the SQLAlchemy engine.
    """
    return engine


def test_database_connection():
    """
    Test PostgreSQL connection.
    """
    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT version();")
        )

        return result.fetchone()[0]


def execute_sql_file(file_path):
    """
    Read and execute an SQL file.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"SQL file not found: {file_path}"
        )

    # Read SQL file using UTF-8
    sql_content = path.read_text(
        encoding="utf-8"
    )

    # Split SQL commands
    statements = [
        statement.strip()
        for statement in sql_content.split(";")
        if statement.strip()
    ]

    # Execute statements
    with engine.begin() as connection:

        for statement in statements:

            connection.exec_driver_sql(
                statement
            )

    print(
        f"SQL executed successfully: {file_path}"
    )