from django.shortcuts import render
import manager
# Create your views here.
def index(request):
	context ={

	}
	
	return render(request,'teacher/teacher_check.html',context)



def record_entry(request):
	context ={}
	

	return render (request,'teacher/record_entry.html',context)




def teacher_record_check(request):

	record_list = manager.check_record(var7 = 2)

	context ={
			'record' : record_list


	}


	return render (request,'teacher/teacher_record_check.html',context)