import mysql.connector
import sys

con = mysql.connector.connect(host="localhost", user="root", passwd="P@r@s2809", database="school", auth_plugin='mysql_native_password')

if con.is_connected():
    print("Successfully Connected...........")
else:
    print("Can't Connect properly")

cur = con.cursor()

print("Cursor object created.....")

print("*" * 50)
sid = int(input("Enter Student ID:"))
sname = input("Enter student First Name:")
lname = input("Enter student Last Name:")
a = int(input("Enter Age:"))
g= float(input("Enter Grade:"))

query = "INSERT INTO stud (student_id, first_name, last_name, age, grade) VALUES ({}, '{}', '{}', {}, {})".format(sid, sname, lname, a, g)

cur.execute(query)
con.commit()

print("Values added to stud table successfully.......!")


select_query = "SELECT * FROM stud"
cur.execute(select_query)

# Fetch all rows and print the results
results = cur.fetchall()
print("Data from stud table:")
for result in results:
    print(result)