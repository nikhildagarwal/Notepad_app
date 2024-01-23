import sqlite3


class DeletePassword:
    def __init__(self, email, password_id):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                                user TEXT, password TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("DELETE FROM passwords WHERE user_id = ? AND password_id = ?", (uid, password_id))
        connection.commit()
        connection.close()


class DeleteAllPasswords:
    def __init__(self, email):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (password_id INTEGER PRIMARY KEY, website TEXT, 
                                user TEXT, password TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("DELETE FROM passwords WHERE user_id = ?", (uid,))
        connection.commit()
        connection.close()
