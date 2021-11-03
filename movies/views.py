import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movie, Showing

# Create your views here.


class IndexView(generic.ListView):
    def get_queryset(self):
        return Showing.objects.order_by("date").filter(date__gte=datetime.date.today())


class MovieDetailView(generic.DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the future showings
        context["showing_list"] = Showing.objects.filter(
            movie=context.get("movie").pk
        ).filter(date__gte=datetime.date.today())
        return context


class ShowingDetailView(generic.DetailView):
    model = Showing

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the future showings
        showing = context.get("showing")
        context["available_seats"] = showing.room.capacity - showing.tickets_sold
        return context
