from django.shortcuts import render

from .models import Link
# Create your views here.

def index (request):
	return render (request, 'index.html')

def link (request):
	link = Link.objects.get(slug=123)
	context = {
		'link' : link,
	}
	return render(request, 'link.html', context)

def url(request, slug):
	link = Link.objects.get (slug=slug)

	context = {
		'link' : link.url,
	}
	return render (request, 'url.html', context)