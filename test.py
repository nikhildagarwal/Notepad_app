import sqlite3
import scripts
from scripts import create_note, add_user, update_note,fetch_notes, fetch_user



string = "https://robinhood.com"
if "://" in string:
    splitted = string.split("://")
    string = "https://" + splitted[1]
else:
    string = "https://"+string


exit(0)

users = ['email.nikhil.agarwal@gmail.com','hopefunfun@gmail.com','nda49@scarletmail.rutgers.edu',
         'as2689@scarletmail.rutgers.edu','ak7.shrivastava@gmail.com']

for user in users:
    fu = fetch_user.FetchUser(user,"")
    print(str(fu.rows))



