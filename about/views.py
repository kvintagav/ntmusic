from django.shortcuts import render , get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from about.models import Actor


# Create your views here.

def hostess(request):
	HOSTESS = Actor.objects.get(name_English__exact='Hostess')
	header = HOSTESS.name 
	return render_to_response('hostess.html',{'actor': HOSTESS , 'header' : header})
	

def chef(request,name):
	CHEF = Actor.objects.get(name_English__exact=name)
	header = CHEF.name
	return render_to_response('chef.html',{'actor':  CHEF , 'header': header})
    
def actors(request):
	header = " Гости музыкального салона"
	return render_to_response('actors.html',{'actors': Actor.objects.filter(chef__exact=False), 'header':header})