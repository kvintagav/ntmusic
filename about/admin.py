from django.contrib import admin
from about.models import Actor

# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    fields = [ 'name','desc','title','chef','name_English']
    list_display = ('name','title')
    list_filter = ['name']

admin.site.register(Actor, ActorAdmin)
