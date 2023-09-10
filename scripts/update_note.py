import sqlite3


class UpdateNote:

    def __init__(self,message_id,message):
        conn = sqlite3.connect('infinote.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, message TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id))''')
        cursor.execute("UPDATE messages SET message = ? WHERE message_id = ?", (message, message_id))
        conn.commit()
        conn.close()
