import sqlite3;

con = sqlite3.connect("homeworkDB.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS workers
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
salary INTEGER)""")

workers = [("Ладюша",18,400), ("Дилярушка",17,500), ("Лейладжон",14,500),
           ("Аделинаджон",16,1000), ("Элинушка",19,500), ("Анюша",15,1000),
           ("Эльзахон",17,2000), ("Амалишка",18,1700), ("Сонюша",16,2540),
           ("Каринушка",16,1890), ("Луизахон",18,2570), ("Настюша (Шеф)",14,1698), ("Иделиябону",19,2578)]
cursor.executemany("INSERT INTO workers (name, age, salary) VALUES (?, ?, ?)", workers)

def taskLimit1(cursor):
    cursor.execute("select * from workers limit 6")
    print(cursor.fetchall())

def taskLimit2(cursor):
    # cursor.execute("select * from workers where id > 1  limit 3")
    cursor.execute("select * from workers limit 3 offset 1")
    print(cursor.fetchall())

def taskOrderBy3(cursor):
    cursor.execute("select * from workers order by salary")
    print(cursor.fetchall())

def taskOrderBy4(cursor):
    cursor.execute("select * from workers order by salary desc")
    print(cursor.fetchall())

def taskOrderBy5(cursor):
    cursor.execute("select * from (select * from workers limit 5 offset 1) order by age")
    print(cursor.fetchall())

def taskCount1(cursor):
    cursor.execute("select count(*) from workers")
    print(cursor.fetchone()[0])

def taskCount2(cursor):
    cursor.execute("select count(*) from workers where salary = 300")
    print(cursor.fetchone()[0])

def taskSelect1(cursor):
    cursor.execute("select * from workers where id = 3")
    print(cursor.fetchall())

def taskSelect5(cursor):
    cursor.execute("select * from workers where salary >= 500")
    print(cursor.fetchall())

def taskSelect8(cursor):
    cursor.execute("select salary, age from workers where name = 'Лейладжон'")
    print(cursor.fetchall())

def taskOrAnd8(cursor):
    cursor.execute("select * from workers where age = 14 or salary != 400")
    print(cursor.fetchall())

# taskLimit1(cursor)
# taskLimit2(cursor)
#
# taskOrderBy3(cursor)
# taskOrderBy4(cursor)
# taskOrderBy5(cursor)
#
# taskCount1(cursor)
# taskCount2(cursor)
#
# taskSelect1(cursor)
# taskSelect5(cursor)
# taskSelect8(cursor)
#
# taskOrAnd8(cursor)