class Student(object):
    """docstring for student

		PARAM:
		(roll number,student name,section,branch,batch)


	"""

    def __init__(self, num, name, section, branch, batch):
        self.uni_num = num
        self.name = name
        self.section = section
        self.batch = batch
        self.branch = branch

    def get_info(self):
        """
		        this function provides the information of the  specific student
		"""
        print(self.uni_num)
        print(self.name)
        print(self.section)
        print(self.batch)
        print(self.branch)


li = {}


def stu_args(x):
    """"
	    this function provides the arguments taken by student one by one
	"""
    return {
        1: "num",
        2: "name",
        3: "section",
        4: "branch",
        5: "batch"
    }[x]


def stu_input():
    """
	this  function  is used to input data of student
	:return: list of  keys(agruments) mapped to their respective value
	"""
    for i in range(1, 6):
        tmp = input("enter the  parameter " + stu_args(i))
        key = stu_args(i)
        li.update({key: tmp})

    return li
