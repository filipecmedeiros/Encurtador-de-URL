from django.shortcuts import render
from random import choice
from string import ascii_uppercase, digits

from .models import Link
from .forms import LinkForm
# Create your views here.

def index (request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			link = form.cleaned_data['link']

			lista = Link.objects.filter(url=link)
			if (lista.count() > 0):
				print ('ja existe')
			else:
				random = ''.join(choice(ascii_uppercase+digits) for i in range(6))
				print (random)
				Link.objects.create(url=link, slug=random)
			
			context = {
				'form' : form,
				'link' : Link.objects.get(url=link)
			}	
	else:
		form = LinkForm()
		context = {
			'form' : form,
		}	

	
	return render (request, 'index.html', context)

def link (request, slug):
	link = Link.objects.get(slug=slug)
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