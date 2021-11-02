from django.contrib import admin
from .models import Movie, Room, Showing

# Register your models here.

admin.site.register([Movie, Room, Showing])
