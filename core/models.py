from django.db import models

# Create your models here.

class Link (models.Model):

	url = models.CharField ('URL', max_length=500)
	slug = models.SlugField ('Identificador', max_length=200)
	