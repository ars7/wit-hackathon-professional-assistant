from django import forms
from .models import List
from .models import Calendar
from .models import Scheduler

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ["item","expected_time","frequency","completed"]

class CalendarForm(forms.ModelForm):
	class Meta:
		model = Calendar
		fields = ["task","day","start_time","end_time"]

class SchedulerForm(forms.ModelForm):
	class Meta:
		model = Scheduler
		fields = ["day","task","start_time","end_time"]

