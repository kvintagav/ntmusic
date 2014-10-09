
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from afisha.models import Event
# Create your views here.

def index(request):
    return render_to_response('top.html')