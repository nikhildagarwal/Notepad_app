import sqlite3

connection = sqlite3.connect('infinote.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("people", rows)

email = rows[0][2]
cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                        user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
uid = cursor.fetchall()[0][0]
cursor.execute("SELECT * FROM messages WHERE user_id = ?", (uid,))
rows = cursor.fetchall()
print("messages", rows)

cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                                user TEXT, password TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
uid = cursor.fetchall()[0][0]
cursor.execute("SELECT * FROM passwords WHERE user_id = ?", (uid,))
rows = cursor.fetchall()
print("passwords", rows)
