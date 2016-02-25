from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	return HttpResponse(u"this is the test.")

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	return HttpResponse(str(c))

def difAdd(request, a,b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_add_redirect(request,a,b):
	return HttpResponseRedirect(reverse('difAdd',args = (a,b)))

def home(request):
	return render(request,'testWeb.html')