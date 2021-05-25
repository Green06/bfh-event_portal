from django.db import models

# Create your models here.

class Participant(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
    

	def __str__(self):
		return self.name


class eventlist(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.TextField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)








	