from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
	context = {}


	return	render(request,'student/student.html',context)