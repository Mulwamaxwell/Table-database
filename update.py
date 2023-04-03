import sqlite3

conn = sqlite3.connect('employee.db')
print("Connected successfully")

conn.execute("UPDATE Staff set SALARY=50000.00 where ID=1")
conn.commit()

data = conn.execute("SELECT * FROM Staff")
for rows in data:
    print("ID: ", rows[0])
    print("FIRSTNAME: ", rows[1])
    print("LASTNAME: ", rows[2])
    print("AGE: ", rows[3])
    print("SALARY: ", rows[4])
    print("TASK: ", rows[5])

print("UPDATED SUCCESSFULLY")
conn.close()