import sqlite3
import scripts
from scripts import create_note, add_user, update_note,fetch_notes, fetch_user

users = ['email.nikhil.agarwal@gmail.com','hopefunfun@gmail.com','nda49@scarletmail.rutgers.edu']

for user in users:
    fu = fetch_user.FetchUser(user,"")
    print(str(fu.rows))



