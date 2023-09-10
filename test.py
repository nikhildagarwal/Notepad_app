import sqlite3
import scripts
from scripts import create_note, add_user, update_note

connection = sqlite3.connect('infinote.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

