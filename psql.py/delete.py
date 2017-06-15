import psycopg2

conn = psycopg2.connect(database = "myproject", user = "myprojectuser", password = "pass", host = "localhost", port = "5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("DELETE from COMPANY where ID=2;")
conn.commit
print "Total number of rows deleted :", cur.rowcount

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