from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from datetime import datetime as dtime, date, time
import datetime
from .models import Calendar
from .forms import CalendarForm
from .models import Scheduler
from .forms import SchedulerForm
import random


# Create your views here.
######################

####### HOME #########

######################
def home(request):
	return render(request,'home.html')

def clean(request):
	List.objects.all().delete()
	Calendar.objects.all().delete()
	Scheduler.objects.all().delete()
	return render(request,'home.html')

######################

####### TODO #########

######################
def todo(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)
		# print(form)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request,('A new task has been added to the list!'))
			return render(request,'todo.html',{'all_items':all_items})
		else :
			messages.success(request,('Fill everything!'))
			all_items = List.objects.all
			return render(request,'todo.html',{'all_items':all_items})
	else :
		all_items = List.objects.all
		return render(request,'todo.html',{'all_items':all_items})

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	# print(item.completed)
	item.delete()
	messages.success(request,("Task has been deleted!"))
	return redirect('todo')


######################

##### CALENDAR #######

######################
def calendar(request):
	if request.method == "POST":
		form = CalendarForm(request.POST or None)
		# print(form)
		if form.is_valid():
			form.save()
			all_items = Calendar.objects.all
			messages.success(request,('Calendar updated!'))
			return render(request,'calendar.html',{'all_items':all_items})
		else :
			messages.success(request,('Fill everything!'))
			all_items = Calendar.objects.all
			return render(request,'calendar.html',{'all_items':all_items})

	else :
		all_items = Calendar.objects.all
		return render(request,'calendar.html',{'all_items':all_items})

def delete_in_calendar(request,list_id):
	item = Calendar.objects.get(pk=list_id)
	item.delete()
	messages.success(request,("Task has been deleted!"))
	return redirect('calendar')

######################

##### SCHEDULER ######

######################
def check_overlap(fixed_start, fixed_end, new_start, new_end):
    overlap = False
    if new_start == fixed_end or new_end == fixed_start:    #edge case
        overlap = False
    elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
        overlap = True
    elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
        overlap = True

    return overlap


def scheduler(request):
	day_map = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
	days = {'Monday':[0 for i in range(48)],'Tuesday':[0 for i in range(48)],'Wednesday':[0 for i in range(48)],
		'Thursday':[0 for i in range(48)],'Friday':[0 for i in range(48)],'Saturday':[0 for i in range(48)],
		'Sunday':[0 for i in range(48)]}
	
	# smart algo : {Morning : 7AM - 11AM, Afternoon : 12PM - 3PM, evening : 5PM-8PM, night : 9PM-12AM}
	morning_activity = ['meditate','breakfast','laundry']
	morning_time = [14,22]
	afternoon_activity = ['make or order lunch','nap']
	afternoon_time = [24,30]
	evening_activity = ['hobby','buy groceries','exercise']
	evening_time = [34,40]
	night_activity = ['make or order dinner','catch-up','video games']
	night_time = [42,48]

	def get_todo():
		all_items = List.objects.values()
		items = len(all_items)
		return all_items

	def get_calendar():
		all_meetings = Calendar.objects.values()
		meetings = len(all_meetings)
		return all_meetings
	
	#add calendar objects to scheduler 
	all_meetings = get_calendar()
	for meeting in all_meetings:
		day = meeting['day']
		task = meeting['task']
		start_time = meeting['start_time']
		end_time = meeting['end_time']
		for j in range(start_time,end_time):
			days[day_map[day]][j] = 1
		print(days)
		Scheduler.objects.create(day=day, task=task, start_time=start_time, end_time=end_time)

	def find_slot(item,duration,day):
		if duration%30 == 0:
			block = duration/30
		else :
			block = duration//30 + 1
		
		if item in morning_activity:
			start_index = morning_time[0]
			end_index = morning_time[0]
			count = 0

			while(start_index<=end_index and end_index<morning_time[1]):
				if days[day_map[day]][end_index] == 0:
					count+=1
					if count == block:
						return [start_index,end_index]
					end_index+=1
				
				else :
					end_index+=1
					start_index = end_index
					count = 0

		elif item in afternoon_activity:
			start_index = afternoon_time[0]
			end_index = afternoon_time[0]
			count = 0
			while(start_index<=end_index and end_index<afternoon_time[1]):
				if days[day_map[day]][end_index] == 0:
					count+=1
					if count == block:
						return [start_index,end_index]
					end_index+=1
				
				else :
					end_index+=1
					start_index = end_index
					count = 0

		elif item in evening_activity:
			start_index = evening_time[0]
			end_index = evening_time[0]
			count = 0
			while(start_index<=end_index and end_index<evening_time[1]):
				if days[day_map[day]][end_index] == 0:
					count+=1
					if count == block:
						return [start_index,end_index]
					end_index+=1
				
				else :
					end_index+=1
					start_index = end_index
					count = 0

		elif item in night_activity:
			start_index = night_time[0]
			end_index = night_time[0]
			count = 0
			while(start_index<=end_index and end_index<night_time[1]):
				if days[day_map[day]][end_index] == 0:
					count+=1
					if count == block:
						return [start_index,end_index]
					end_index+=1
				
				else :
					end_index+=1
					start_index = end_index
					count = 0

		else :
			start_index = 14
			end_index = 14
			count = 0
			while(start_index<=end_index and end_index<48):
				if days[day_map[day]][end_index] == 0:
					count+=1
					if count == block:
						return [start_index,end_index]
					end_index+=1
				
				else :
					end_index+=1
					start_index = end_index
					count = 0

		return None
			
	all_items = get_todo()
	for item in all_items:
		frequency = item['frequency']
		for day in range(frequency):
			slot = find_slot(item['item'],item['expected_time'],day+1)
			if slot == None :
				print("Can not schedule this task in your calendar")
			else :
				for j in range(slot[0],slot[1]+1):
					days[day_map[day+1]][j] = 1
					print(days)
				Scheduler.objects.create(day=day+1, task=item['item'], start_time=slot[0], end_time=slot[1]+1)

	List.objects.all().delete()
	Calendar.objects.all().delete()
	all_items = Scheduler.objects.all
	return render(request,'scheduler.html',{'all_items':all_items})
