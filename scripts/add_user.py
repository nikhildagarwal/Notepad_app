import sqlite3

from scripts import my_crypt


class AddUser:

    def __init__(self, name, email, password, phone):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if len(cursor.fetchall()) == 0:
            c = my_crypt.MyCrypt(password,email)
            c.encrypt()
            cursor.execute("INSERT INTO users (name, email, password, phone) VALUES (?, ?, ?, ?)",
                           (name, email, c.output, phone))
            connection.commit()
            self.done = True
        else:
            self.done = False
        connection.close()



