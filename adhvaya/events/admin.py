from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Participant)
admin.site.register(eventlist)
#admin.site.register(order)
	