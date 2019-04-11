from django.shortcuts import render
from .models import Student

import manager
# Create your views here.
def index(request):
	context = {}


	return	render(request,'student/student.html',context)


def record_entry(request):
	context = {}

	return render(request, 'student/record_entry.html',context)


def stu_record_check(request):
	record_list = manager.check_record(var7 = 1)
	
	context = {
		'record' : record_list,
		'range'  : range(0,5),
	}

	return render(request,'student/stu_record_check.html',context)



def student_entry(request):

	""" 
	process data from form
	"""
	
	number,name,branch,batch,section = None,None,None,None,None
	
	roll_number = request.POST.get('roll_number')
	name = request.POST.get('name')
	section =  request.POST.get('section')
	branch = request.POST.get('branch')
	batch = request.POST.get('batch')
	
	print(name)
	print(section)

	boole = manager.student_entry(roll_number,name,section,branch,batch)


	context = {
	'roll_number': roll_number,
	'name': name,
	'section': section,
	'branch' : branch,
	'batch': batch,
	'bool' : boole,

	}


	return render(request,'student/student_entry.html',context)