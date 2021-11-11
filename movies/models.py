from django.db import models
from django.contrib import admin
from django.utils import timezone
from django_countries.fields import CountryField
import datetime

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    cast = models.TextField()
    release_year = models.CharField(max_length=4, default=datetime.date.today().year)
    director = models.CharField(max_length=200)
    country = CountryField(blank_label="Select country", default="FR")
    description = models.TextField()
    d = datetime.timedelta(days=0, hours=1, minutes=30, seconds=0)
    duration = models.DurationField(default=d)
    ratings = [
        ("E", "Everyone"),
        ("T", "Teens"),
        ("A", "Adults only"),
    ]
    rating = models.CharField(max_length=1, choices=ratings, default="E")
    trailer_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Showing(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField("projection date")
    time = models.TimeField("projection time")
    languages = [("VO", "VOST"), ("VF", "VF")]
    language = models.CharField(max_length=2, choices=languages, default="VF")
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie} le {self.date} à {self.time} dans la salle {self.room}."

    @admin.display(
        ordering="date",
        description="Future showing?",
        boolean=True,
    )
    def is_showing_in_the_future(self):
        today = timezone.now().date()
        return self.date >= today
