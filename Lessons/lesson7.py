# СУБД - Система Управления Базой Данных
# БД - База Данных

import sqlite3

def create_connection(db_name):
    connection = sqlite3.connect(db_name)
    return connection

create_connection("Geeks.db")

def create_table(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    
def create_students(con, student: tuple):
    sql = """INSERT INTO Geeks_14_2B
    (full_name, date, visit, is_passed, characteristics)
    VALUES (?,?,?,?,?);
    """
    cursor = con.cursor()
    cursor.execute(sql, student)
    con.commit()    

sql_create_table = """
CREATE TABLE IF NOT EXISTS Geeks_14_2B (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR (70) NOT NULL,
date DATE NOT NULL,
visit DOUBLE (2, 1) DEFAULT 0.0,
is_passed BOOLEAN DEFAULT FALSE,
characteristics TEXT DEFAULT NULL
);
"""

connection = create_connection("Geeks.db")

if connection:
    print("Успешное соединение")
    create_table(connection, sql_create_table)
    create_students(connection, ("Ахмадбек уулу Элизар", "2024", 1.0, False, "Красавчик"))