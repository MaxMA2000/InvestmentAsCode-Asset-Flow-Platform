import os
from dotenv import load_dotenv
from typing import Dict, Any, Callable
import psycopg2

load_dotenv()


class PostgresManager():
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self) -> None:
        """connect the POSTGRES database with config set in .env
        """
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            database=os.getenv("POSTGRES_DATABASE"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        self.cursor = self.conn.cursor()

    def close(self):
        """close the cursor and conn
        """
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

    def commit(self):
        """commit the executions
        """
        if self.conn is not None:
            self.conn.commit()
