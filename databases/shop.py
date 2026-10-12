import sqlite3
from pathlib import Path


def connect():
    db_path = Path(__file__).parent / "webshop.db"
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,)
    )
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Price must be a number and stock a whole number. Product not saved.")
        return
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock),
    )
    conn.commit()
    print("Saved!")


def change_stock(conn):
    product_id = int(input("Product id: "))
    new_stock = int(input("New stock: "))
    cursor = conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, product_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        print(f"No product with id {product_id}.")
    else:
        print(f"Stock for product {product_id} set to {new_stock}.")


def show_receipt(conn):
    order_id = int(input("Which oder id: "))
    cursor = conn.execute(
        """
        SELECT p.name, oi.quantity, oi.quantity * oi.unit_price AS sum_price
        FROM order_items oi
        JOIN products p ON p.product_id = oi.product_id
        WHERE oi.order_id = ?
        """,
        (order_id,),
    )
    rows = cursor.fetchall()

    if not rows:
        print(f"No order with id {order_id}.")
        return

    total = 0
    for name, quantity, sum_price in rows:
        print(f"{name:<20} {quantity:>3} x  = {sum_price:>8.2f} kr")
        total += sum_price

    print(f"{'TOTAL':<20} {total:>16.2f} kr")


def main():
    conn = connect()
    while True:
        print(
            "\n1) List products  2) Search customers  3) Add product  4) Change stock 5) Show order receipt 0) Quit"
        )
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "0":
            break
    conn.close()


main()
