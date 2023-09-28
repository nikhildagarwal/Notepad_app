import sqlite3


class FetchNotes:
    def __init__(self, email):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                        user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("SELECT * FROM messages WHERE user_id = ?",(uid,))
        self.rows = cursor.fetchall()


