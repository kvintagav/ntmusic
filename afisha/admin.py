from django.contrib import admin
from afisha.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['event_name', 'event_date', 'event_visitors','event_desc']
    list_display = ('event_name', 'event_date', 'event_visitors','event_desc')
    list_filter = ['event_date']

admin.site.register(Event, EventAdmin)
