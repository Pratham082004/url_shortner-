import sqlite3

DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        long_url TEXT NOT NULL,
        short_code TEXT UNIQUE
    )
    """)

    conn.commit()
    conn.close()


def insert_url(long_url):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("INSERT INTO urls (long_url) VALUES (?)", (long_url,))
    conn.commit()

    url_id = cur.lastrowid
    conn.close()
    
    return url_id


def save_short_code(url_id, short_code):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("UPDATE urls SET short_code=? WHERE id=?", (short_code, url_id))
    conn.commit()
    conn.close()


def get_long_url(short_code):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT long_url FROM urls WHERE short_code=?", (short_code,))
    result = cur.fetchone()
    conn.close()

    return result[0] if result else None