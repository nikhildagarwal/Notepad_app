import sqlite3


class DeleteNote:
    def __init__(self, email, message_id):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("DELETE FROM messages WHERE user_id = ? AND message_id = ?", (uid, message_id))
        connection.commit()
        connection.close()


class DeleteAllNotes:
    def __init__(self, email):
        connection = sqlite3.connect('infinote.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, title TEXT, message TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
        uid = cursor.fetchall()[0][0]
        cursor.execute("DELETE FROM messages WHERE user_id = ?", (uid, ))
        connection.commit()
        connection.close()
