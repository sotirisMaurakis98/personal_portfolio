from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
	projects = Project.objects.all() # gets all the objects of type projects from data base
	return render(request, 'portfolio/home.html', {'projects':projects})
