import mysql.connector as mysql

db = mysql.connect(
	host = 'localhost',
	user = 'root',
    port = '3306',
	password = 'kartik@1234',

)

mycursor = db.cursor()

#mycursor.execute("CREATE DATABASE myattendance")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

mycursor.execute("USE ATTENDANCE")
sql = "INSERT INTO attendance(serial , name ,mark) VALUES (%s, %s, %s)"
val = ( "1","Highway 21","p")
mycursor.execute(sql, val)


mycursor.execute("SELECT * FROM attendance")


for x in mycursor:
	print(x)


