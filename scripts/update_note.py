import sqlite3


class UpdateNote:

    def __init__(self,message_id,message,title):
        conn = sqlite3.connect('infinote.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                                (user_id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, phone TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (message_id INTEGER PRIMARY KEY, message TEXT, 
                                user_id INT, FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE)''')
        cursor.execute("UPDATE messages, title SET message = ?, title = ? WHERE message_id = ?", (message, title, message_id))
        conn.commit()
        conn.close()
