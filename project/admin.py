from django.contrib import admin

# Register your models here.
from .models import Event, Venue, Dance

admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Dance)