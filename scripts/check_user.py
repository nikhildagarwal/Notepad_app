import sqlite3


class CheckUser:

    def __init__(self, email):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if len(cursor.fetchall()) > 0:
            self.exists = True
        else:
            self.exists = False
