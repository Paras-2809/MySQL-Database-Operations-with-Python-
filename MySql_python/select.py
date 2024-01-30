import mysql.connector
import sys

con = mysql.connector.connect(host="localhost", user="root", passwd="P@r@s2809", database="school", auth_plugin='mysql_native_password')

if con.is_connected():
    print("Successfully Connected...........")
else:
    print("Can't Connect properly")

cur = con.cursor()
query = "SELECT * FROM stud "
cur.execute(query)
results = cur.fetchall()
for result in results:
    print(result)

   


