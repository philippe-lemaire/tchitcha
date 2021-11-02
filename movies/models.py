from django.db import models
import datetime

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    cast = models.TextField()
    release_year = models.CharField(max_length=4, default=datetime.date.today().year)
    description = models.TextField()
    ratings = [
        ("E", "Everyone"),
        ("T", "Teens"),
        ("A", "Adults only"),
    ]
    rating = models.CharField(max_length=1, choices=ratings, default="E")

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
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.movie} le {self.date} à {self.time} dans la salle {self.room}."
