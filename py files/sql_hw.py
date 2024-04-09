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

# cursor.execute("select * from workers limit 6")
# print(cursor.fetchall())

# cursor.execute("select * from workers where id > 1  limit 3")
# print(cursor.fetchall())

# cursor.execute("select * from workers order by salary")
# print(cursor.fetchall())

# cursor.execute("select * from workers order by salary desc")
# print(cursor.fetchall())

# cursor.execute("select * from (select * from workers limit 5 offset 1) order by age")
# print(cursor.fetchall())

# cursor.execute("select count(*) from workers")
# print(cursor.fetchone()[0])

# cursor.execute("select count(*) from workers where salary = 300")
# print(cursor.fetchone()[0])

# cursor.execute("select * from workers where id = 3")
# print(cursor.fetchall())

# cursor.execute("select * from workers where salary != 500")
# print(cursor.fetchall())

# cursor.execute("select salary, age from workers where name = 'Лейладжон'")
# print(cursor.fetchall())

# cursor.execute("select * from workers where age = 14 or salary != 400")
# print(cursor.fetchall())