from django.contrib import admin
from .models import Movie, Room, Showing

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    search_fields = ["title", "release_year"]
    list_display = ["title", "rating", "genre", "release_year"]
    list_filter = ["genre", "rating"]


class ShowingAdmin(admin.ModelAdmin):
    list_display = [
        "movie",
        "is_showing_in_the_future",
        "date",
        "time",
        "room",
        "tickets_sold",
    ]
    list_filter = ["date"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Showing, ShowingAdmin)
admin.site.register(Room)
