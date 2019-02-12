class student(object):
	"""docstring for student"""
	def __init__(self, arg):
		super(student, self).__init__()
		self.arg = arg


#example for attendance %
attended_days = 50
total_days = 176

def attendance_calculator(attended,total):
	z = ((attended / total)*100).__round__(2)

	return z

attendance_percentage= attendance_calculator(attended_days,total_days)
print(attendance_percentage)