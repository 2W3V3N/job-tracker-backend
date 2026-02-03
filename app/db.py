import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "jobtracker.db"

def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT NOT NULL,
                applied_on TEXT NOT NULL,
                link TEXT,
                notes TEXT
            )
            """
        )
        conn.commit()
