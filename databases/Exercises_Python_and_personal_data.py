import sqlite3
from pathlib import Path

# Excercise 1

# db_path = Path(__file__).parent / "webshop.db"
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# cursor.execute("SELECT first_name, last_name, city FROM customers")
# for first_name, last_name, city in cursor.fetchall():
#     print(f"{first_name} {last_name}, {city}")

# conn.close()

# Excersise 2

# db_path = Path(__file__).parent / "webshop.db"
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# max_price = input("Maxpris: ")

# cursor.execute("SELECT name, price FROM products WHERE price < ?", (max_price,))
# for name, price in cursor.fetchall():
#     print(f"{name}: {price}")

# conn.close()

# Excersise 3
# import sqlite3
# from pathlib import Path

# db_path = Path(__file__).parent / "webshop.db"
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# category = input("Write a category: ")

# cursor.execute("SELECT name, price FROM products WHERE category = ?", (category,))
# for name, stock in cursor.fetchall():
#     print(f"{name}: {stock} st")

# conn.close()

# Excersise 4
# Explain in your own words: why is building SQL with an f-string dangerous,
# and why is a ? placeholder safe?

# User input could contain SQL code. With a placeholder the database engine
# treats it strictly as a value, so the code is never parsed or executed.

# Excersise 5
