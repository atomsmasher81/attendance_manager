import mysql.connector as mysql

"""
connecting to the mysql server
"""

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    port = '3306',
    password = 'kartik@1234',

)

mycursor = db.cursor()

"""
#mycursor.execute("CREATE DATABASE myattendance")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

#mycursor.execute("USE ATTENDANCE")

"""


def check_tables():
    """
    check the required tables and if they are not present creating them
    """
    print("checking for required tables")
    mycursor.execute("USE attendance")
    #mycursor.execute("alter table attendance modify column mark varchar(2) default 'A'")
    mycursor.execute("SHOW TABLES")
    temp = []
    for x in mycursor:

        temp.append(x)

    if mycursor.arraysize != 3:

        attendance_table = 0
        student_table = 0
        teacher_table = 0
    
        for x in temp:
            for y in x:


                if y == 'attendance':
                    attendance_table = 1
                    print("attendance table exists")
                if y == 'student':
                    student_table = 1
                    print("student table exists")
                if y == 'teacher':
                    teacher_table = 1
                    print("teacher table exists")

        if attendance_table == 0:
            mycursor.execute("CREATE TABLE attendance(serial varchar(2) , name varchar(20) FOREIGN KEY REFERENCES student(name),mark varchar(2) DEFAULT 'A')")
            print("attendance table created")
        if student_table == 0:
            mycursor.execute("CREATE TABLE Student(roll_number varchar(10) PRIMARY KEY,name varchar(20) ,section varchar(5),branch varchar(5),batch varchar(4))")
            print("student table created")
        if teacher_table == 0:
            mycursor.execute (
                "CREATE TABLE Teacher(number varchar(5) PRIMARY KEY,name varchar(20),branch varchar(5))")
            print("teacher table created")

        


def all_record(profile):
    mycursor.execute('SELECT * FROM %s'%(profile))
    result = mycursor.fetchall()
    for x in result:
        print(x)

def specific_record(proflie,name):
    #sql ='SELECT * FROM %s WHERE NAME=%s ' % (tuple(proflie,name)
    try:
        mycursor.execute("SELECT * FROM %s WHERE name='%s' " % (proflie,name))


    except :
        print("person not in records")
    else:
        result = mycursor.fetchall()
        for x in result:
            print(x)

try:
    mycursor.execute("SELECT * FROM attendance ORDER BY SERIAL DESC LIMIT 1")
except:
    print("there is no  existing record ")



def  all_stu():
    mycursor.execute("SELECT name FROM Student")
    stu_list= []
    for x in mycursor:
        stu_list.append(x)
    return stu_list

def insert_teacher(li):

        placeholders = ', '.join(['%s'] * len(li))
        columns = ', '.join(li.keys())
        sql = "INSERT INTO teacher ( %s ) VALUES ( %s )" % ( columns, placeholders)
        #sql = "INSERT INTO teacher (number ,name,branch ) VALUES (%s, %s,%s)"
       # li1 = t
        mycursor.execute(sql, tuple(li.values()))


def insert_student(li):
    placeholders = ', '.join(['%s'] * len(li))
    columns = ', '.join(li.keys())
    sql = "INSERT INTO student ( %s ) VALUES ( %s )" % ( columns, placeholders)
    mycursor.execute(sql,tuple( li.values()))


def mark(stu,mark):

    sql = "INSERT "
    #sql = "UPDATE TABLE attendance SET mark = '%s' WHERE NAME = '%s'" %tuple((mark,stu))

    mycursor.execute(sql)



def bye():
    db.commit()
"""
mycursor.execute("SELECT * FROM attendance")


for x in mycursor:
    print(x)
"""

