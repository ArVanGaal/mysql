import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hochzeit2309",
    database="testdb"
)

mycursor = mydb.cursor()

sql = "UPDATE students SET age=13 WHERE name ='Bob'"

mycursor.execute("SELECT * FROM students LIMIT 3 OFFSET 2")

myresult =mycursor.fetchall()

for result in myresult:
    print (result)