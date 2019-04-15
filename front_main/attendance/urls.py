from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name = 'attendance'),
	path('attendance_entry/',views.attendance_entry,name= 'attendance_entry'),
	path('attendance_check/',views.attendance_check,name ='attendance_check'),
	path('attendance_sucess/',views.attendance_sucess,name= 'attendance_sucess')
]