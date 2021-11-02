from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    cover_url = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    cast = models.TextField()
    description = models.TextField()
    ratings = [
        ("E", "Everyone"),
        ("T", "Teens"),
        ("A", "Adults only"),
    ]
    rating = models.CharField(max_length=1, choices=ratings, default="E")


class Room(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()


class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField("projection date")
    time = models.TimeField("projection time")
    tickets_sold = models.IntegerField(default=0)
