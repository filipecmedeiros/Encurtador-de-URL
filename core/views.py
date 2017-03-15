from django.shortcuts import render

# Create your views here.

def index (request):
	return render (request, 'index.html')

def link(request):
	return render (request, 'link.html')