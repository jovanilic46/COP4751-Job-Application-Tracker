"""MySQL access helpers. All values use bound parameters."""
import os
from contextlib import contextmanager
import mysql.connector
from dotenv import load_dotenv
load_dotenv(override=True)

@contextmanager
def connection():
    conn = mysql.connector.connect(host=os.getenv('DB_HOST','localhost'), user=os.getenv('DB_USER','root'), password=os.getenv('DB_PASSWORD',''), database=os.getenv('DB_NAME','job_tracker'))
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def query(sql, params=(), one=False):
    with connection() as conn:
        cur=conn.cursor(dictionary=True)
        try:
            cur.execute(sql, params)
            return cur.fetchone() if one else cur.fetchall()
        finally: cur.close()

def execute(sql, params=()):
    with connection() as conn:
        cur=conn.cursor()
        try:
            cur.execute(sql, params)
            return cur.lastrowid
        finally: cur.close()
