import sqlite3

import scripts.update_user

# Connect to the database
conn = sqlite3.connect('infinote.db')

# Create a cursor
cursor = conn.cursor()

# Create a table

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

