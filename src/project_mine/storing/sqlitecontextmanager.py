import sqlite3

class SQLiteContextManager:

    """context manager for SQLite db, handling opening and closing of the connection"""

    def __init__(self, db_path: str) -> None:
       self.db_path = db_path
       self.connection = None

    def __enter__(self):
        """establish the connection with the db

        Returns:
            cursor: return the cursor for executing the queriess
        """
        self.connection = sqlite3.connect(self.db_path)
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """commit and closing the connection"""
        self.connection.commit()
        self.connection.close()
