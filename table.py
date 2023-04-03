import sqlite3

conn = sqlite3.connect('employee.db')
print("connected successfully")

conn.execute("""CREATE TABLE Staff1(
ID INT PRIMARY KEY NOT NULL ,
FIRSTNAME TEXT NOT NULL ,
LASTNAME TEXT NOT NULL ,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(20))""")

print("successfully created Staff table")
conn.close()