from django.contrib import admin
from afisha.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['name', 'date', 'visitors','desc']
    list_display = ('name', 'date', 'visitors','desc')
    list_filter = ['date']

admin.site.register(Event, EventAdmin)
