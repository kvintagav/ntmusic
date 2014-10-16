from django.shortcuts import render , get_object_or_404
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from about.models import Actor


# Create your views here.

def chef(request,name):
    return render_to_response('chef.html',{'events': Event.objects.get(name__exact=name)})

