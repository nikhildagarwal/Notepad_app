import sqlite3
import scripts
from scripts import create_note, add_user

connection = sqlite3.connect('infinote.db')
cursor = connection.cursor()
cursor.execute('SELECT messages.message, users.email FROM users INNER JOIN messages ON users.user_id = messages.user_id')
rows = cursor.fetchall()
for row in rows:
    print(row)

