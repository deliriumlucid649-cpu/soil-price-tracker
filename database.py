import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('soil_prices.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create tables

# Table for products
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    retailer_id INTEGER,
    FOREIGN KEY (retailer_id) REFERENCES retailers (id)
)
''')

# Table for prices
cursor.execute('''
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    price REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products (id)
)
''')

# Table for retailers
cursor.execute('''
CREATE TABLE IF NOT EXISTS retailers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    url TEXT
)
''')

# Table for price history
cursor.execute('''
CREATE TABLE IF NOT EXISTS price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price_id INTEGER,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (price_id) REFERENCES prices (id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()