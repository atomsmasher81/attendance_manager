class Teacher(object):

    def __init__(self, teach_num, name, branch, special_designation=None):
        self.teach_num = teach_num
        self.name = name
        self.branch = branch
        self.special_designation = special_designation

    def get_info(self):
        """
        this function provides the information of the  specific teacher
        """
        print(self.teach_num)
        print(self.name)
        print(self.branch)
        print(self.special_designation)


li = {}


def teach_args(x):
    """"
    this function provides the arguments taken by teacher  one by one
    """
    return {
        1: "number",
        2: "name",
        3: "branch",
        4: "special_degsination"
    }[x]


def teach_input():
    """
    this  function  is used to input data of teacher
    :return: list of  keys(agruments) mapped to their respective value
    """
    for i in range(1, 4):
        tmp = input("enter the  teacher's " + teach_args(i))
        key = teach_args(i)
        li.update({key: tmp})

    return li
