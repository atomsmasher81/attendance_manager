from django.shortcuts import render
import manager
# Create your views here.


def index(request):
	context ={

	}
	
	return render(request,'teacher/teacher_check.html',context)



def record_entry(request):
	"""
	render form to input data
	"""
	#global number,name,branch

	context = {}

	return render (request,'teacher/record_entry.html',context)




def teacher_record_check(request):

	record_list = manager.check_record(var7 = 2)

	context ={
			'record' : record_list


	}


	return render (request,'teacher/teacher_record_check.html',context)





def teacher_entry(request):

	""" 
	process data from form
	"""
	#global number,name,branch
	number,name,branch = None,None,None
	
	number = request.POST.get('Number')
	name = request.POST.get('Name')
	branch = request.POST.get('Branch')
	context ={}



	
	
	boole = manager.teach_entry(number,name,branch)


	context = {
	'number': number,
	'name': name,
	'branch' : branch,
	'bool' : boole,

	}


	return render(request,'teacher/teacher_entry.html',context)