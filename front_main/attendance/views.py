from django.shortcuts import render
import manager
# Create your views here.









def index(request):
	context = {}


	return render (request,'pages/attendance.html',context)



def attendance_entry(request):

	context={}

	return render (request,'pages/attendance_entry.html',context)



def attendance_check(request):
	att,names  =manager.check_att()
	#stu =student.object.all()
	y = len(names)
	
	context = {
		'atte' : att,
		'name' : names,
		'y': y,
		'range' : range(1,y+1),
	}

	 
	print(context['name'][0])

	return render (request, 'pages/attendance_check.html',context)



