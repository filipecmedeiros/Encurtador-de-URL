from django.db import models

from django.core.urlresolvers import reverse
# Create your models here.

class Link (models.Model):

	url = models.CharField ('URL', max_length=500)
	slug = models.SlugField ('Identificador', max_length=200)

	def __str__ (self):
		return self.slug

	def get_absolute_url (self):
		return reverse('url', kwargs={'slug':self.slug,})
	