import sqlite3
from flask import g

def connect_to_database():
    sqlite3.connect("user_database.db")
    sqlite3.row_factory = sqlite3.Row
    return sqlite3

def get_database():
    if not hasattr(g, 'user_data_db'):
        g.sqlite_db = connect_to_database()
    return g.sqlite_db    