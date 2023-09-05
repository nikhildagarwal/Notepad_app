import sqlite3


class AddUser:

    def __init__(self, name, email, password):
        connection = sqlite3.connect('../infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if len(cursor.fetchall()) == 0:
            cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            connection.commit()
            self.done = True
        else:
            self.done = False
        connection.close()
