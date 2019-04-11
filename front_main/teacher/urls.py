from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name = 'teacher_check'),
	path('record_entry/',views.record_entry,name= 'record_entry_teach'),
	path('teacher_record_check',views.teacher_record_check,name = 'teacher_record_check'),
	path('teacher_entry/',views.teacher_entry,name= 'teacher_entry'),
]