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

# Excersise 7
# float("abc") will throw an error.


# Excersise 9

# SELECT DISTINCT products.name
# FROM orders
# JOIN order_items ON order_items.order_id = orders.id
# JOIN products ON products.id = order_items.product_id
# WHERE orders.customer_id = 1

# Excersise 10
# UPDATE customers
# 	SET email = "erik.johansson@example.com"
# 	WHERE first_name = "Erik"

# Excersise 11
# DROP VIEW IF EXISTS customer_overview;
# CREATE VIEW customer_overview AS
# SELECT c.customer_id,
#        c.first_name,
#        c.city,
#        COUNT(o.order_id) AS order_count
# FROM customers c
# LEFT JOIN orders o ON o.customer_id = c.customer_id
# GROUP BY c.customer_id, c.first_name, c.city;

# SELECT * FROM customer_overview;

# Excersise 12
# Discuss in pairs: the webshop wants to add a birth_date column 'just in case'. What would you
# say? Write two sentences.

# I would say we should not collect personal data “just in case” — only when
# we know we actually need it. Under the GDPR principle of data minimization,
#  you may only collect personal data for a specific purpose, and every extra
# column of sensitive data is an unnecessary risk if the database ever leaks.
