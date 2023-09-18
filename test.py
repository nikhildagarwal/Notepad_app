import sqlite3
import scripts
from scripts import create_note, add_user, update_note,fetch_notes

fn1 = fetch_notes.FetchNotes("email.nikhil.agarwal@gmail.com")
fn2 = fetch_notes.FetchNotes("nda49@scarletmail.rutgers.edu")
for row in fn1.rows:
    print(row)
for row in fn2.rows:
    print(row)


