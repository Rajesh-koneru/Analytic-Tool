from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3

from select import select

DATABASE = "database.db"

# Create a connection and a table
def create_table():
    query=f"""create table sales(Date date ,amount integer ,region varchar(30))"""
    conn = sqlite3.connect(DATABASE)
    pointer=conn.cursor()
    pointer.execute(query)
    conn.commit()
    conn.close()
    print('table created...')

#for showing table in base
def show_tables():
    query="""SELECT name FROM sqlite_master WHERE type='table';
"""
    conn = sqlite3.connect(DATABASE)
    pointer = conn.cursor()
    pointer.execute(query)
    tables=pointer.fetchall()
    print(f" tables are {tables}")
    conn.commit()
    conn.close()

def delete_table(name):
    query=f"""drop table {name} """
    conn = sqlite3.connect(DATABASE)
    pointer = conn.cursor()
    pointer.execute(query)
    print('table deleted successfully')

def show_data(table):
    query=f"""select * from {table}"""
    conn = sqlite3.connect(DATABASE)
    pointer = conn.cursor()
    pointer.execute(query)
    data=pointer.fetchall()
    print(f"data is {data}")

def insert_data():
    query = """INSERT INTO sales (Date, sale, region) VALUES (?, ?, ?)"""

    data = [
        ("2025-05-01", 123400, "north"),
        ("2025-06-01", 600000, "south"),
        ("2025-07-01", 900000, "north"),
        ("2025-08-01", 3030043, "east")
    ]

    conn = sqlite3.connect(DATABASE)
    pointer = conn.cursor()

    # ✅ Use executemany() for multiple inserts
    pointer.executemany(query, data)

    # Commit changes
    conn.commit()

    print("Data inserted successfully")

    # Close connection
    conn.close()
def show_data1():
    query=f"""select * from sales where Date='2025-01-01'"""
    conn = sqlite3.connect(DATABASE)
    pointer = conn.cursor()
    pointer.execute(query)
    data=pointer.fetchall()
    print(f"data is {data}")
show_data1()

def main(select):
    if select==1:
        create_table()
    elif select==2:
        show_tables()
    elif select==3:
        table=input('enter the table name to be delete')
        delete_table(table)
    elif select==4:
        table=input('enter table name')
        show_data(table)
    elif select==5:
        insert_data()
    else:
        print('enter valid number...')

num=int(input('enter the number'))
main(num)


