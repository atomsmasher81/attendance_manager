from django.shortcuts import render

# Create your views here.
def index(request):
	context ={

	}
	
	return render(request,'teacher/teacher.html',context)



def record_entry(request):
	context ={}
	

	return render (request,'teacher/record_entry.html',context)