import Profile.Student as Student
import Profile.Teacher as Teacher
import db
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

"""
list of all the functions in this program and their short briefing

1. main_menu() : main menu
2.all_mark         : to mark all attendance together
3.one_mark      : to mark attendance of one student
4.enter_record  : to enter record
5. mark_att        : parent funtion to mark attendance
6. att_cal           :  to calculate %
7.call_main        : to call main menu
8.bye                : exiting the attendance manager
9.check_record : checking the record
10.check_att        :to check attendance 
11. plot              : to plot the graph
"""

date =  None

def plot(dates,start_date,var9,flag):
    # for plotting graph
    dict = {}
    counter = 0
    temp_date = []
    for x in dates:

        if x == start_date:
            counter += 1

        if counter == 1:
            temp_date.append(x)
            pr, ab, mrk, unused_start_date = db.check_att(var9, temp_date, flag)
            att = att_cal(pr, ab)
            dict[x] = att

        else:

            dict[x] = 0
    # rng = np.arange(0,100,10)


    plt.plot(dict.keys(), dict.values(), color='black', markevery=1, markerfacecolor='blue', marker='o')

    plt.xlabel("dates")
    plt.ylabel("percentage")
    plt.title("attendance graph")
    plt.show()


def check_att(*args,**kwargs):

    var9 = None
    all = 0
    flag =3
    # flag =int( input("enter name or roll number of  student you want to check attendance for\n"
    #       "1. name \n"
    #       "2. roll number\n"
    #       "3. attendance list of all student"))
    if flag == 1:
         var9 = input("enter the name of student")
    elif flag == 2:
        var9 = input("enter the roll number of student")
    elif flag == 3:
        all = 1
    else:
        print("invalid input")
        check_att()

    dates = db.give_dates()
    if all ==1:


        li_val = []
        li =  db.all_stu()
        for x in li:
            present, absent, mark, start_date = db.check_att(x, dates, all)

            att = att_cal(present, absent)

            li_val.append(att)
        print(li_val)
        dict_name = []
        dict_att =[]

        dict1= {'name' : li ,'att'  : li_val}
        return dict1,li

    else:
        present, absent, mark, start_date = db.check_att(var9, dates, flag)

        att = att_cal(present, absent)
        print("attendance is {}".format(att))
        var6 = input("do u want to see the graph of the latter\n"
                    "y : yes \n"
                    "").upper()
        if var6 == 'Y':
            plot(dates, start_date, var9, flag)

    call_main()

def check_record(*args,**kwargs):
    for keys,values in kwargs.items():

        var7 = values
    #var7  =1
    record_list = []
    # var7=int( input("do you want to check teacher or student record\n"
    #             "1. student\n"
    #             "2.teacher\n"))


    if var7 == 2:
        a = 'teacher'
        # var8 = int(input("you want to check:\n "
        #                  "1.all record \n"
        #                  "2.specific"))
        # if var8 ==1:
        #     print("list of all teacher are")

        record_list = db.all_record(a)
        # elif var8 ==2:
        #     var9 = input("enter the name")
        #     db.specific_record(a,var9)
        # else:
        #     print("incorrect option")
        #     check_record()
    elif var7 == 1:
        a = 'student'
        # var8 = int(input("you want to check:\n "
        #                  "1.all record \n"
        #                  "2.specific"))
        # if var8 == 1:
        #     print("list of all student are")

        record_list =  db.all_record(a)

        # elif var8 == 2:
        #     var9 = input("enter the name")
        #     db.specific_record(a, var9)
        # else:
        #     print("incorrect option")
        #     check_record()

    return record_list
    #call_main()


def bye():
    global main_menu_count
    print("you visited main menu {} times".format(main_menu_count))
    print("thanks for using attendance manager \n"
          "Exiting...")
    db.bye()

def call_main():
    global main_menu_count
    main_menu_count+=1
    main_menu()

def main_menu():

    """
    C'mon, you get it by the name

    """
    if  main_menu_count == 1:
        print("hey , Welcome to your attendance manager. \n")
    else :
        print("Welcome back to main menu")
    print(" Here is the stuff you can do -\n"
          " 1.add teacher or student record\n "
          "2.check teacher or student record\n"
          "3. mark attendance\n"
          "4.check attendance\n"
          "5.exit"
          )
    var6 = int(input())
    if var6 == 1:
        enter_record()
    elif var6 == 2:
        check_record()

    elif var6 == 3:
        mark_att()

    elif var6 == 4:
        check_att()
    elif var6 == 5:
        bye()





def all_mark(date):
    """

    to mark attendance of all student one by one
    :return:
    """
    flag =1  #this define that attendance is by name
    stu_list =db.all_stu()
    for y in stu_list:


        print("mark attendance for ", y)
        mark =input().upper()
        if mark != 'P' and  mark != 'A':
            print("this attendance mark is not allowed")
            all_mark(date)
        db.mark(y,mark,flag,date)
    call_main()


def one_mark(date):

    """
    to mark the attendance of  a student
    :return:
    """
    var4 = int(input("do you want to mark attendance by name or roll number \n 1.name \n 2.roll number"))
    if var4 ==1:
            var5 = input("enter the name of the full  student")
            mark = input("enter : \n P--> Present \n A --> Absent").upper()
            db.mark(var5,mark,var4)

    elif var4 == 2:
            var5 = input("enter the roll number of the student")
            mark = input("enter : \n P--> Present \n A --> Absent").upper()
            db.mark(var5,mark,var4)

    else:
        print("invalid input")
        one_mark()
    print("attendance marked")






def enter_record():

    var1 = int(input("select profile\n"
          "1. Teacher\n"
          "2. Student"))


    if var1==1:

        li = Teacher.teach_input()
        db.insert_teacher(li)
        print("record created")

        """
        creating the object for teacher
        

        #t1 = Teacher.Teacher(**li)
        """



    else:
        li = Student.stu_input()
        db.insert_student(li)
        print("record created")
        


        """
        creating the object for student
        
        
        s1 = Student.Student(**li)

        """
    call_main()


def mark_att():
    """
    for marking the attendance
    """


    global date
    print("ok, let's get started with this")
    x =  str(dt.datetime.now().date())

    print("enter the date of attendance\n"
               "or use current date{}".format(x))
    input_date=int(input("1.custom date \n"
               "2.current date"))

    if input_date == 1:
        date = input("enter date\n"
                     "yyyy-mm-dd")
    elif input_date == 2:
        date = x




    var3 = int(input("for all student or particular one \n 1. all student \n 2. particular one"))

    if var3 == 1:
        all_mark(date)

    elif var3== 2:
        var7 = 'y'
        while var7 == 'y':
            one_mark(date)
            print("do you want to mark attendance for another student : "
                  "Enter 'y' if yes else press any other key ")
            var7 = input().lower()
    else:
        print("invalid option")
        mark_att()
    call_main()







def att_cal(attended,absent):
    z = ((attended / (attended + absent))*100).__round__(2)

    return z



if __name__ == '__main__':

    db.check_tables()

    main_menu_count = 1

    main_menu()


