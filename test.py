import sqlite3

connection = sqlite3.connect('infinote.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("people", rows)


cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                        user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
cursor.execute("SELECT * FROM messages")
rows = cursor.fetchall()
print("messages", rows)

cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                                user TEXT, password TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
cursor.execute("SELECT * FROM passwords")
rows = cursor.fetchall()
print("passwords", rows)
