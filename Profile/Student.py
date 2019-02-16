class Student(object):
	"""docstring for student

		PARAM:
		(roll number,student name,section,branch,batch)


	"""
	def __init__(self,num, name,section,branch,batch):
		self.uni_num = num
		self.name = name
		self.section = section
		self.batch = batch
		self.branch = branch


	def get_info(self):
		print(self.uni_num)
		print(self.name)
		print(self.section)
		print(self.batch)
		print(self.branch)


li = {}

def stu_args(x):
	return {
		1 : "num",
		2 : "name",
		3 : "section",
		4: "branch",
		5: "batch"
	}[x]


def stu_input():
    for i in range(1, 6):
        tmp = input("enter the  parameter " + stu_args(i))
        key = stu_args(i)
        li.update({key: tmp})

    return li