import mysql.connector
import sys

con = mysql.connector.connect(host="localhost", user="root", passwd="P@r@s2809", database="school", auth_plugin='mysql_native_password')

if con.is_connected():
    print("Successfully Connected...........")
else:
    print("Can't Connect properly")

cur = con.cursor()





sname = input("Enter student First Name:")
new_grade = float(input("Enter the new Grade:"))

# Use placeholders in the query to prevent SQL injection
query = "UPDATE stud SET Grade = %s WHERE first_name = %s"
    
# Pass the values as a tuple to execute method
values = (new_grade, sname)

cur.execute(query, values)
con.commit()

if cur.rowcount > 0:
    print("Grade updated successfully for {}.......!".format(sname))
else:
    print("No record found for {}.......!".format(sname))

select_query = "SELECT * FROM stud"
cur.execute(select_query)

# Fetch all rows and print the results
results = cur.fetchall()
print("Data from stud table:")
for result in results:
    print(result)

    