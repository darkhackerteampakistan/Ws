# database.py

import sqlite3
import os
from datetime import datetime

DB_DIR = "database"
DB_FILE = os.path.join(DB_DIR, "messages.db")


def init_database():
    os.makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT UNIQUE,
            created_at TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_contact(name, phone):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO contacts
            (name, phone, created_at)
            VALUES (?, ?, ?)
            """,
            (
                name,
                phone,
                datetime.now().isoformat()
            )
        )

        conn.commit()

    except sqlite3.IntegrityError:
        pass

    conn.close()


def get_contacts():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, phone
        FROM contacts
        ORDER BY id DESC
    """)

    rows = cur.fetchall()
    conn.close()

    return rows


def add_log(event):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO logs
        (event, created_at)
        VALUES (?, ?)
        """,
        (
            event,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()


def get_logs(limit=50):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, event, created_at
        FROM logs
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cur.fetchall()
    conn.close()

    return rows


if __name__ == "__main__":
    init_database()

    add_contact("Test User", "8801000000000")
    add_log("Database initialized")

    print("Contacts:")
    for row in get_contacts():
        print(row)

    print("\nLogs:")
    for row in get_logs():
        print(row)
