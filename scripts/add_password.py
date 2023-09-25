import sqlite3
from scripts import my_crypt


def check_not_valid(str1, str2):
    max_num = 0
    for char in str1:
        num = ord(char)
        if num > max_num:
            max_num = num
    for char in str2:
        num = ord(char)
        if num > max_num:
            max_num = num
    if max_num >= 123:
        return True
    return False


class AddPassword:

    def __init__(self, email, website, user, password):
        if check_not_valid(user, password):
            self.error = "username and password must not contain: ~ } { |"
            return
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                        user TEXT, password TEXT, 
                        user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        rows = cursor.fetchall()
        if len(rows) == 0:
            self.error = "no id found for email"
        else:
            user_id = rows[0][0]
            c1 = my_crypt.MyCrypt(user, email)
            c2 = my_crypt.MyCrypt(password, email)
            c1.encrypt()
            c2.encrypt()
            cursor.execute("INSERT INTO passwords (website, user, password, user_id) VALUES (?, ?, ?, ?)",
                           (website, c1.output, c2.output, user_id))
            connection.commit()
            connection.close()
            self.error = None
