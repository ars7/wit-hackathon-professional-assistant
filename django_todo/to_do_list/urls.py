from django.urls import path
from . import views

urlpatterns = [
	path('home/',views.home,name='home'),
	path('',views.clean,name='clean'),
	path('todo/',views.todo, name='todo'),
	path('calendar/',views.calendar,name='calendar'),
	path('scheduler/',views.scheduler,name='scheduler'),
	# path('analytics/',views.analytics,name='analytics'),
	path('delete_list/<list_id>',views.delete, name ='delete'),
	path('delete_calendar/<list_id>',views.delete_in_calendar, name ='delete_in_calendar'),
]