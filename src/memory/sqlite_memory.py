import sqlite3
from pathlib import Path


class SQLiteMemory:
    def __init__(self):
        db_path = Path("database/memory.db")
        db_path.parent.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
            """
        )
        self.connection.commit()

    def save(self, key: str, value: str):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO memories
            (key, value)
            VALUES (?, ?)
            """,
            (key, value),
        )
        self.connection.commit()

    def get(self, key: str):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT value
            FROM memories
            WHERE key=?
            """,
            (key,),
        )
        result = cursor.fetchone()
        return result[0] if result else None

