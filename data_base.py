# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("Bot_Data_Base.db")
cursor = connection.cursor()

def creates():
    cursor.execute("""CREATE TABLE table_description
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        description TEXT)
                        """)

def insert():
    cursor.execute("INSERT INTO table_description (name, description) VALUES ('', '')")
    connection.commit()

def select_description(name_key):
    cursor.execute(f"SELECT description FROM table_description WHERE name=\"{name_key}\"")
    description = cursor.fetchone()
    return description