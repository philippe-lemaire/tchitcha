import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movie, Showing

# Create your views here.


class IndexView(generic.ListView):
    context_object_name = "future_showing_list"

    def get_queryset(self):
        return Showing.objects.order_by("date").filter(date__gte=datetime.date.today())


class DetailView(generic.DetailView):
    model = Movie
