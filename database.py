# database.py

import sqlite3
import os
from datetime import datetime
from config import DATABASE_FILE


def connect():
    return sqlite3.connect(DATABASE_FILE)


def init_database():
    conn = connect()
    cur = conn.cursor()

    # Contacts table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT UNIQUE,
            created_at TEXT
        )
    """)

    # Logs table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT,
            created_at TEXT
        )
    """)

    # Messages tracking table (optional for API status)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            message TEXT,
            status TEXT,
            message_id TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


# ---------------- CONTACTS ----------------

def add_contact(name, phone):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT OR IGNORE INTO contacts (name, phone, created_at)
        VALUES (?, ?, ?)
    """, (name, phone, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, name, phone FROM contacts ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()
    return rows


# ---------------- LOGS ----------------

def add_log(event):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO logs (event, created_at)
        VALUES (?, ?)
    """, (event, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def get_logs(limit=50):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, event, created_at
        FROM logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- MESSAGES ----------------

def save_message(phone, message, status="pending", message_id=None):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO messages (phone, message, status, message_id, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (phone, message, status, message_id, datetime.now().isoformat()))

    conn.commit()
    conn.close()


def update_message_status(message_id, status):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE messages
        SET status = ?
        WHERE message_id = ?
    """, (status, message_id))

    conn.commit()
    conn.close()


def get_messages(limit=50):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, phone, message, status, created_at
        FROM messages
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- TEST ----------------

if __name__ == "__main__":
    init_database()
    add_contact("Test User", "8801712345678")
    add_log("Database initialized")
    print(get_contacts())
    print(get_logs())
