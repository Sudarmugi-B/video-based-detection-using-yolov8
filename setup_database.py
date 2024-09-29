import sqlite3

# Create/connect to the database file
conn = sqlite3.connect('detected_frames.db')
cursor = conn.cursor()

# Create a table to store detected frame names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS detected_frames (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        frame_name TEXT
    )
''')

conn.commit()
conn.close()