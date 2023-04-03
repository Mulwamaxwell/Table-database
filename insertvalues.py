import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected")

conn.execute("INSERT INTO Staff1(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
              VALUES(11,'Maxwell','Mark',27,45000.00,'Employer')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(12,'Ian','Ann',20,45000.00,'Employer1')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
            VALUES(13,'Wilson','Mugwe',26,46000.00,'Employer2')")
conn.execute("INSERT INTO Staff(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
             VALUES(14,'Gerald','Max',24,47000.00,'Employer3')")

conn.commit()
print("Successfully inserted values into Staff table")

conn.close()