import mysql.connector as mysql

"""
connecting to the mysql server
"""

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    port = '3306',
    password = 'XXXX',

)

mycursor = db.cursor()
attendance_serial = None
databases= []

mycursor.execute("SHOW DATABASES")
result = mycursor.fetchall()
for x in result:
    for y in x:
        databases.append(y)


if  'attendance' in  databases:
    print("database exists")

else:
    mycursor.execute('CREATE DATABASE attendance')
    print("database created")
mycursor.execute('USE ATTENDANCE')



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
        if student_table == 0:
            mycursor.execute("CREATE TABLE Student(roll_number varchar(10) PRIMARY KEY,name varchar(20) ,section varchar(5),branch varchar(5),batch varchar(4))")
            print("student table created")
        if attendance_table == 0:
            mycursor.execute("CREATE TABLE attendance(serial varchar(2) , name varchar(20),roll_number varchar(5) ,mark varchar(2) DEFAULT 'A',FOREIGN KEY(roll_number) REFERENCES student(roll_number)) ")

            print("attendance table created")

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


def mark(stu,mark,flag):
    """

    :param stu:
    :param mark:
    :param flag: to check that input given is by name (VAL:1)or by roll num(VAL:2)

    :return:
    """
    create_att_table()
    global attendance_serial
    record_exist =[]
    mycursor.execute("SELECT roll_number FROM STUDENT")
    result= mycursor.fetchall()
    for x in result:
        record_exist.append(x)

    if record_exist != None:
        if flag == 1:

            mycursor.execute("UPDATE ATTENDANCE SET MARK = '%s'  WHERE NAME = '%s'"%(mark,stu) )
        else:
            mycursor.execute("UPDATE ATTENDANCE SET MARK = '%s'  WHERE roll_number = '%s'" % (mark, stu))


    else:


        li1= []


        mycursor.execute("SELECT serial FROM attendance ORDER BY SERIAL DESC LIMIT 1")


        result = mycursor.fetchall()
        for x in result:
            if x != None:
                attendance_serial=x+1

        if attendance_serial is None:
            attendance_serial =1
        """

         sql =  "SELECT CASE WHEN EXISTS (SELECT serial FROM attendance ORDER BY SERIAL) THEN CAST (1 AS BIT) ELSE CAST (0 AS A BIT)"
        mycursor.execute(sql)
         """

        li1.append(attendance_serial)
        mycursor.execute("SELECT name,roll_number FROM student ")
        for x in mycursor:
            for y in x:
                li1.append(y)


        li1.append(mark)
        sql = "INSERT   INTO  attendance(SERIAL,NAME,ROLL_NUMBER,MARK) VALUES (%s, '%s', %s,'%s')" %tuple(li1)
        #sql = "UPDATE TABLE attendance SET mark = '%s' WHERE NAME = '%s'" %tuple((mark,stu))

        mycursor.execute(sql)

def create_att_table():
    attendance_serial1 =1
    var =1
    count = 0
    roll_nums = []
    name =[]
    mycursor.execute('SELECT roll_number,name FROM student ')
    result= mycursor.fetchall()
    for x in result:
        for y in x:
            if  count/2 == 0:
                roll_nums.append(y)
                count+=1
            else:
                name.append(y)
                count+=1

    total = len(result)
    while var >= total:
        mycursor.execute("INSERT   INTO  attendance(SERIAL,NAME,ROLL_NUMBER,MARK) VALUES (%s, '%s', %s)"%(var,name[x],roll_nums[x],))
        var+=1


def bye():
    db.commit()
"""
mycursor.execute("SELECT * FROM attendance")


for x in mycursor:
    print(x)
"""

