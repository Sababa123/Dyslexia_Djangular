

from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.views import View




def angular_view(request):

	template_name = 'index.html'
	
	context = { }
	return render(request, template_name, context)

def register_view(request):
    
	template_name = 'register/index.html'
	
	context = { }
	return render(request, template_name, context)
