import psycopg2

conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "pass", host = "localhost", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit
print "Total number of rows updated :", cur.rowcount

cur.execute("SELECT id, name,age, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "Age = ", row[2]
   print "ADDRESS = ", row[3]
   print "SALARY = ", row[4], "\n"

print "Operation done successfully";
conn.close()