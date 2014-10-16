from django.shortcuts import render , get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from afisha.models import Event
from django.utils import timezone

# Create your views here.

def all(request):
    return render_to_response('all.html',{'events': Event.objects.all()})

def coming(request):
	all_events=Event.objects.filter(date__gte=timezone.now())
	events_column=[]
	for index in range(len(all_events)):
		event = []
		event.append(index%2)
		event.append(all_events[index])
		events_column.append(event)

	return render_to_response('coming.html',{'events':events_column})
	

def event(request,event_id=1):
	try:
		event_id=int(event_id)
	except ValueError:
		raise Http404()
	#сделать проверку на наличие события иначе сказать что такого нет 
	return render_to_response('event.html', {'event': Event.objects.get(id=event_id)})


def archives(request):
    return HttpResponse("hello archives")


def response(request):
	return HttpResponse("Текущая страница %s" % request.path)
