import sqlite3
from pathlib import Path

from sympy import limit


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
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
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
        return result[0] if result else None   #

    def set_preference(self, key: str, value: str):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT OR REPLACE INTO preferences
            (key, value)
            VALUES (?, ?)
            """,
            (key, value),
        )
        self.connection.commit()

    def get_preference(self, key: str):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT value
            FROM preferences
            WHERE key=?
            """,
            (key,),
        )
        result = cursor.fetchone()
        return result[0] if result else None   #same pattern

    def list_preferences(self):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            SELECT key, value
            FROM preferences
            """
        )


    def add_history(
        self,
        command
        ):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO command_history
            (command)
            VALUES (?)
            """,
            (command,)
        )

        self.connection.commit()

        cursor.execute(
            """
            DELETE FROM command_history
            WHERE id NOT IN (
                SELECT id
                FROM command_history
                ORDER BY id DESC
                LIMIT 25
            )
            """
        )

        self.connection.commit()


    def get_history(
        self,
        limit=None
):

        cursor = self.connection.cursor()

        query = """
        SELECT command
        FROM command_history
        ORDER BY id DESC
        """

        if limit:
            query += f" LIMIT {limit}"

        cursor.execute(query)

        return cursor.fetchall()
