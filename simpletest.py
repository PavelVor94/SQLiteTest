import sqlite3

def db_connect():
    return sqlite3.connect('mydatabase.db')


def createTabl():
    con = db_connect()
    curs = con.cursor()
    curs.execute('CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)')
    con.commit()



def paste_in_table():
    con = db_connect()
    curs = con.cursor()
    curs.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    entities = (2, 'Andrew' , 800, 'IT' , 'Tech' , '2018-02-06')
    curs.execute("INSERT INTO employees(id,name,salary,department,position,hireDate) VALUES(?,?,?,?,?,?)" , entities)
    con.commit()



def update_table():
    con = db_connect()
    curs = con.cursor()
    curs.execute("UPDATE employees SET name = 'Rogers' where id = '2'")
    con.commit()


def select_table(tablename):
    con = db_connect()
    curs = con.cursor()
    curs.execute("SELECT * FROM "+tablename)
    rows = curs.fetchall()
    for row in rows:
        print(row)

def many_paste():
    con = db_connect()
    curs = con.cursor()
    curs.execute('CREATE TABLE IF NOT EXISTS projects(id integer, name text)')
    data = [(1, "Ridesharing"), (2, 'Water Purifying'), (3, 'Forensics'), (4, 'Botany')]
    curs.executemany('INSERT INTO projects VALUES(?,?)' , data)
    con.commit()



select_table('employees')


