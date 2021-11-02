import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Movie, Showing

# Create your views here.


def index(request):
    future_showing_list = Showing.objects.order_by("date").filter(
        date__gte=datetime.date.today()
    )
    context = {"future_showing_list": future_showing_list}
    return render(request, "movies/index.html", context)


def detail(request, movie_id):
    # detail view for a movie
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/details.html", {"movie": movie})
