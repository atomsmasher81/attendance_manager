from django.shortcuts import render
import manager
# Create your views here.









def index(request):
	context = {}


	return render (request,'pages/attendance.html',context)



def attendance_entry(request):
	att,names  =manager.check_att()
	date = manager.current_date()
	#stu =student.object.all()
	y = len(names)
	
	context = {
		'atte' : att,
		'name' : names,
		'y': y,
		'range' : range(1,y+1),
		'date' : date,
	}


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



def attendance_sucess(request):

	att,names= manager.check_att()
	date = request.POST.get('date')
	mark =[]
	c = 1
	boole = None
	print(boole)

	for x in names:
		
		temp =	request.POST.get('mark' + str(c))
		c+=1
		mark.append(temp)
	print("attendance_sucess")
	print(mark)
	try:

		manager.all_mark_front(names,mark,date)

	except:
		boole = False
	else:
		boole = True 
	manager.bye()
	context = {

		'boole' : boole,
	}
	print(context['boole'])
	return render (request,'pages/services.html',context)