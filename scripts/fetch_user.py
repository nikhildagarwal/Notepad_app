import sqlite3

EMAIL = 0
PASSWORD = 1


class FetchUser:

    def __init__(self, email, password):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            self.name = None
            self.email = None
            self.error = EMAIL
        else:
            row = rows[0]
            if row[3] == password:
                self.name = row[1]
                self.email = row[2]
                self.error = None
            else:
                self.name = None
                self.email = None
                self.error = PASSWORD
        connection.close()
