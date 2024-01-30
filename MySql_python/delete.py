import mysql.connector
import sys

con = mysql.connector.connect(host="localhost", user="root", passwd="P@r@s2809", database="school", auth_plugin='mysql_native_password')

if con.is_connected():
    print("Successfully Connected...........")
else:
    print("Can't Connect properly")

cur = con.cursor()
print("*" * 50)

lname = input("Enter student Last Name:")
query = "DELETE FROM stud WHERE last_name = '{}'".format(lname)

    
cur.execute(query)
con.commit()

    
select_query = "SELECT * FROM stud"
cur.execute(select_query)

# Fetch all rows and print the results
results = cur.fetchall()
print("Remaining Data from stud table:")
for result in results:
    print(result)


