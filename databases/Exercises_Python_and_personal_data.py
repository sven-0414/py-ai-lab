import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "webshop.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
for first_name, last_name, city in cursor.fetchall():
    print(f"{first_name} {last_name}, {city}")

conn.close()
