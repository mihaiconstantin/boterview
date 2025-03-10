# Imports.
from peewee import Proxy, SqliteDatabase


# Create a `sqlite3` database connection.
database: Proxy = Proxy()


# Initialize the `sqlite3` database connection.
def initialize_database(name: str) -> None:
    # Initialize the database connection.
    database.initialize(SqliteDatabase(name, pragmas = {"foreign_keys": 1}))
