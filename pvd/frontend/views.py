from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hello_world(request):
	return render(request, 'hello_world.html')