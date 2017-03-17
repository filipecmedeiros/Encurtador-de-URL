from django.contrib import admin

# Register your models here.

from .models import Link 

class LinkAdmin(admin.ModelAdmin):
	list_display = ['url', 'slug']
	search_fields = ['name', 'slug']


admin.site.register(Link, LinkAdmin)