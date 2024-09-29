import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('user_credentials.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store user credentials if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT
    )
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
