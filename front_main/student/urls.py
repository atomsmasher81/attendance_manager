from django.urls import path
from . import views


urlpatterns = [
	path('',views.index,name = 'student'),
	path('record_entry/',views.record_entry,name= 'record_entry')
]