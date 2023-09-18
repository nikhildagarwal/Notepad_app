import sqlite3

from scripts import my_crypt


class UpdateUser:

    def __init__(self,email):
        self.email = str(email)
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                        (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute("SELECT name FROM users WHERE email = ?", (email,))
        self.name = cursor.fetchall()[0][0]
        connection.commit()
        connection.close()

    def update_password(self,password):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        c = my_crypt.MyCrypt(password, self.email)
        c.encrypt()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute("UPDATE users SET password = ? WHERE email = ?",(c.output,self.email))
        connection.commit()
        connection.close()




