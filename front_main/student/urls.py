from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name = 'student'),
	path('record_entry/',views.record_entry,name= 'record_entry'),
	path('stu_record_check/',views.stu_record_check,name= 'stu_record_check')
]