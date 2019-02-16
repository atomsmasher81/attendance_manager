


class Teacher(object):

    def __init__(self, teach_num, name, branch, special_designation=None):
        self.teach_num = teach_num
        self.name = name
        self.branch = branch
        self.special_designation = special_designation




    def get_info(self):
        print(self.teach_num)
        print(self.name)
        print(self.branch)
        print(self.special_designation)


li = {}

def teach_args(x):
	 return {
		1 : "teach_num",
		2 : "name",
		3: "branch",
		4 : "special_degsination"
	    }[x]

def teach_input():
    for i in range(1, 4):
        tmp = input("enter the  parameter " + teach_args(i))
        key = teach_args(i)
        li.update({key: tmp})

    return li


