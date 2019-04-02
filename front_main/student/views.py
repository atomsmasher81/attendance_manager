from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
	context = {}


	return	render(request,'student/student.html',context)


def record_entry(request):
	context = {}

	return render(request, 'student/record_entry.html',context)