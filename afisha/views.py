from django.shortcuts import render , get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from afisha.models import Event
# Create your views here.

def all(request):
    return render_to_response('all.html',{'events': Event.objects.all()})

def coming(request):
	return render_to_response('coming.html',{'events': Event.objects.all()})

def event(request,event_id=1):
	try:
		event_id=int(event_id)
	except ValueError:
		raise Http404()
	#сделать проверку на наличие события иначе сказать что такого нет 
	return render_to_response('event.html', {'event': Event.objects.get(id=event_id)})


def archives(request):
    return HttpResponse("hello archives")


