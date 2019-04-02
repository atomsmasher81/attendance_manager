from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name = 'Teacher'),
	path('record_entry/',views.record_entry,name= 'record_entry_teach')
]