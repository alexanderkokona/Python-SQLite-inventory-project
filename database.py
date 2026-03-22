import sqlite3

DB_NAME = "inventory.db"

def connect():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    with connect() as conn:
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())

def add_product(name, quantity, price):
    with connect() as conn:
        conn.execute(
            "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )

def get_all_products():
    with connect() as conn:
        cursor = conn.execute("SELECT * FROM products")
        return cursor.fetchall()

def update_product(product_id, quantity, price):
    with connect() as conn:
        conn.execute(
            "UPDATE products SET quantity=?, price=? WHERE id=?",
            (quantity, price, product_id)
        )

def delete_product(product_id):
    with connect() as conn:
        conn.execute(
            "DELETE FROM products WHERE id=?",
            (product_id,)
        )

# Stretch Challenge: Aggregate functions
def get_inventory_summary():
    with connect() as conn:
        cursor = conn.execute("""
            SELECT 
                SUM(quantity * price) as total_value,
                AVG(price) as avg_price,
                COUNT(*) as total_products
            FROM products
        """)
        return cursor.fetchone()