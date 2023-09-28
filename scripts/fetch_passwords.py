import sqlite3
from scripts import my_crypt


class FetchPasswords:

    def __init__(self, email):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                                user TEXT, password TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("SELECT * FROM passwords WHERE user_id = ?",(uid,))
        rows = list(cursor.fetchall())
        self.rows = []
        for row in rows:
            self.rows.append(list(row))
            curr_row = self.rows[-1]
            c1 = my_crypt.MyCrypt(curr_row[2],email)
            c2 = my_crypt.MyCrypt(curr_row[3],email)
            c2.decrypt()
            c1.decrypt()
            curr_row[2] = c1.output
            curr_row[3] = c2.output
