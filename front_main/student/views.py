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