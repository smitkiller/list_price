from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	name = 'Smit Killer'
	return render(request, 'home.html', {'name':name})