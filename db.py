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
        att_date_record = 0
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
                if y == 'att_table_record' :
                    att_date_record = 1
                    print("attendance date record exits")

        if student_table == 0:
            mycursor.execute("CREATE TABLE Student(roll_number varchar(10) PRIMARY KEY,name varchar(20) ,section varchar(5),branch varchar(5),batch varchar(4))")
            print("student table created")
        if attendance_table == 0:
            mycursor.execute("CREATE TABLE attendance(serial varchar(5) , name varchar(20),roll_number varchar(5) ,mark varchar(2) DEFAULT 'A',FOREIGN KEY(roll_number) REFERENCES student(roll_number)) ")

            print("attendance table created")

        if teacher_table == 0:
            mycursor.execute (
                "CREATE TABLE Teacher(number INT AUTO_INCREMENT PRIMARY KEY,name varchar(20),branch varchar(5))")
            print("teacher table created")
        if att_date_record ==0:
            mycursor.execute(
                "CREATE TABLE att_table_record(serial INT AUTO_INCREMENT PRIMARY KEY,date_val varchar(12))"
            )
            print("att_table_record table created")


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




"""
    finally:
        sql ="INSERT INTO att_table_record(date_val) VALUES({})".format(table_name)
        mycursor.execute(sql)

"""

def give_dates():
    dates= []
    sql = "SELECT date_val FROM att_table_record"
    mycursor.execute(sql)
    for x in mycursor:
        for y in x:
            dates.append(y)
    return dates



def check_att(name,dates):
    mark = []

    for x in dates:

        sql = "SELECT MARK FROM `{}`".format(x)
        mycursor.execute(sql)
        for y in mycursor:
            for z in y:
                mark.append(z)

    present = mark.count('P')
    absent = mark.count('A')
    return present,absent
"""           
    for x in mark:
        for y in x:
            if y == 'p'
            present +=1
            absent = mark.count('A')
     """





def create_att_table(date):

    var =0
    count = 0
    roll_nums = []
    name =[]
    mycursor.execute('SELECT roll_number,name FROM student ')
    result= mycursor.fetchall()
    for x in result:
        for y in x:
            if  count%2 == 0:
                roll_nums.append(y)
                count+=1
            else:
                name.append(y)
                count+=1

    total = len(result)


    try:
        mycursor.execute(
            "CREATE TABLE `{}`(serial varchar(3), name varchar(20),roll_number varchar(5) UNIQUE,mark varchar(2) DEFAULT 'A',FOREIGN KEY(roll_number) REFERENCES student(roll_number)) ".format(date)
        )

    except mysql.errors.ProgrammingError:
        print("table {} exist".format(date))

    else:
        sql = "INSERT INTO att_table_record(date_val) VALUES('{}')".format(date)
        mycursor.execute(sql)
        while var < total:
            mycursor.execute("INSERT   INTO  `%s`(SERIAL,NAME,ROLL_NUMBER) VALUES (%s, '%s', %s)" % (
            date, (var + 1), name[var], roll_nums[var],))
            var += 1








def mark(stu,mark,flag,date):
    """

    :param stu:
    :param mark:
    :param flag: to check that input given is by name (VAL:1)or by roll num(VAL:2)

    :return:
    """
    create_att_table(date)
    global attendance_serial
    record_exist =[]
    mycursor.execute("SELECT roll_number FROM STUDENT")
    result= mycursor.fetchall()
    for x in result:
        record_exist.append(x)

    if record_exist != None:
        if flag == 1:

            mycursor.execute("UPDATE `%s` SET MARK = '%s'  WHERE NAME = '%s'"%(date,mark,stu) )
        else:
            mycursor.execute("UPDATE `%s` SET MARK = '%s'  WHERE roll_number = '%s'" % (date,mark, stu))


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




def bye():
    db.commit()
"""
mycursor.execute("SELECT * FROM attendance")


for x in mycursor:
    print(x)
"""

