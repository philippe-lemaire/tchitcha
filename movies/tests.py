import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Movie, Showing, Room


# Create your tests here.

today = datetime.date.today()


def create_room(name):
    return Room.objects.create(name=name, capacity=100)


def create_movie(title):
    cover_url = "some_url"
    genre = "some_genre"
    cast = "That cast"
    release_year = 1999
    description = "awesome description"
    rating = "E"

    return Movie.objects.create(
        title=title,
        cover_url=cover_url,
        genre=genre,
        cast=cast,
        description=description,
        release_year=release_year,
        rating=rating,
    )


def create_showing(date):
    room = create_room("test_room")
    movie = create_movie("test_movie")
    time = timezone.now()
    return Showing.objects.create(room=room, movie=movie, date=date, time=time)


class MoviesIndexTests(TestCase):
    def test_no_showings(self):
        """If there is no showings, display an appropriate text"""
        response = self.client.get(reverse("movies:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucune projection n’est planifiée.")

    def test_past_showings_not_displayed(self):
        date = today - datetime.timedelta(days=1)
        create_showing(date=date)
        response = self.client.get(reverse("movies:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucune projection n’est planifiée.")
