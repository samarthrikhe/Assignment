
import sqlite3
import threading

# Database connection functions
def connect_users_db():
    return sqlite3.connect('users.db')

def connect_products_db():
    return sqlite3.connect('products.db')

def connect_orders_db():
    return sqlite3.connect('orders.db')

# Insertion functions
def insert_users(data):
    conn = connect_users_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, email TEXT)')
    cursor.executemany('INSERT INTO users (id, name, email) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

def insert_products(data):
    conn = connect_products_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER, name TEXT, price REAL)')
    cursor.executemany('INSERT INTO products (id, name, price) VALUES (?, ?, ?)', data)
    conn.commit()
    conn.close()

def insert_orders(data):
    conn = connect_orders_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER, user_id INTEGER, product_id INTEGER, quantity INTEGER)')
    cursor.executemany('INSERT INTO orders (id,user_id, product_id, quantity) VALUES (?,?, ?, ?)', data)
    conn.commit()
    conn.close()

# Data for insertion
users_data = [
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', 'bob@example.com'),
    (3, 'Charlie', 'charlie@example.com'),
    (4, 'David', 'david@example.com'),
    (5, 'Eve', 'eve@example.com'),
    (6, 'Frank', 'frank@example.com'),
    (7, 'Grace', 'grace@example.com'),
    (8, 'Alice', 'alice@example.com'),
    (9, 'Henry', 'henry@example.com'),
    (10, None, 'jane@example.com')
]

products_data = [
    (1, 'Laptop', 1000.00),
    (2, 'Smartphone', 700.00),
    (3, 'Headphones', 150.00),
    (4, 'Monitor', 300.00),
    (5, 'Keyboard', 50.00),
    (6, 'Mouse', 30.00),
    (7, 'Laptop', 1000.00),
    (8, 'Smartwatch', 250.00),
    (9, 'Gaming Chair', 500.00),
    (10, 'Earbuds', -50.00)
]

orders_data = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6 , 6, 6, 4),
    (7 , 7, 7, 2),
    (8, 8, 8, 0),
    (9 , 9, 9, -1),
    (10 , 10, 10, 2)
]

# Thread creation
threads = []
threads.append(threading.Thread(target=insert_users, args=(users_data,)))
threads.append(threading.Thread(target=insert_products, args=(products_data,)))
threads.append(threading.Thread(target=insert_orders, args=(orders_data,)))

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Output results
print("Users, Products, and Orders have been inserted successfully.")
