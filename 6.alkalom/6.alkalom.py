import random
import sqlite3
with sqlite3.connect('test.db') as conn:
    print("Opened database successfully")
    try:
        conn.execute('''CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 AGE            INT     NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL);''')
    except sqlite3.OperationalError as e:
        print(f"Table already exists: {e}")
    try:
        conn.execute(r"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', "
                     r"20000.00 );")
        conn.execute(r"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 );")
        conn.execute(r"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );")
        conn.execute(r"INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', "
                     r"65000.00 );")
        conn.commit()
        print("Records created successfully")
    except sqlite3.IntegrityError as e:
        print(f"Values are already existing: {e}")
    try:
        conn.execute(f"UPDATE COMPANY set SALARY = {random.randint(20000, 100000)} where ID = 1")
        conn.commit()
    except Exception as e:
        print(f"Cannot Update salary: {e}")
    print("Total number of rows updated :", conn.total_changes)
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3], "\n")
    print(cursor)
    conn.execute("DELETE from COMPANY where ID = 2;")
    conn.commit()