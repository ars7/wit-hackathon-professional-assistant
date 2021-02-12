from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class List(models.Model):
	item = models.CharField(max_length = 200)
	expected_time = models.IntegerField(default = 15,blank=True)
	frequency = models.IntegerField(default=1,blank=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		# return self.item + '|' + str(self.completed)
		return self.item + '|' + str(self.expected_time) + '|' + str(self.frequency) + '|' + str(self.completed)

class Calendar(models.Model):
	task = models.CharField(max_length = 200, default='This is the default task')
	day = models.IntegerField(default=7)
	start_time = models.IntegerField(default = 14)
	end_time = models.IntegerField(default = 15)

class Scheduler(models.Model):
	task = models.CharField(max_length = 200, default='This is the default task')
	day = models.IntegerField(default=7)
	start_time = models.IntegerField(default = 14)
	end_time = models.IntegerField(default = 15)
		
	
