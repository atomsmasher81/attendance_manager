import Profile.Student as Student
import Profile.Teacher as Teacher


print("do you want to enter record : y/n")
var = input().lower()
if var== 'y':
	var1 =input("select profile"
		  "1. Teacher"
		  "2. Student")


	if var1==1:
		li = Teacher.teach_input()
		t1 = Teacher.Teacher(**li)
	else:
		li = Student.stu_input()
		s1 = Student.Student(**li)









#example for attendance %
attended_days = 50
total_days = 176

def attendance_calculator(attended,total):
	z = ((attended / total)*100).__round__(2)

	return z

attendance_percentage= attendance_calculator(attended_days,total_days)
print(attendance_percentage)

