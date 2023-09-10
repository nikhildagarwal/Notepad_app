import sqlite3


class CreateNote:

    def __init__(self, email, note, title):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                        user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id))''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?",(email,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            self.error = "no id found for email"
        else:
            user_id = rows[0][0]
            cursor.execute("INSERT INTO messages (title, message, user_id) VALUES (?, ?, ?)",
                           (title, note, user_id))
            connection.commit()
            connection.close()
            self.error = None

