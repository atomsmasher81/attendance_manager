from django.shortcuts import render
import manager
# Create your views here.



def index(request):
	return render(request, 'pages/index.html')


def about(request)	:
	return render(request,'pages/about.html')

def contact(request):
	return render(request,'pages/contact.html')

def services(request):
	manager.check_tables()
	return render(request,'pages/services.html')
	
