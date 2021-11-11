import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Movie, Showing
from .forms import BuyTicketsForm

# Create your views here.


class IndexView(generic.ListView):
    def get_queryset(self):
        return Showing.objects.order_by("movie", "date", "time").filter(
            date__gte=datetime.date.today()
        )


def buy_tickets(request, showing_id):
    showing = get_object_or_404(Showing, pk=showing_id)
    max_amount = showing.room.capacity - showing.tickets_sold

    if request.method == "POST":
        # create the form and populate it
        form = BuyTicketsForm(request.POST)
        if form.is_valid():
            asked_tickets = form.cleaned_data.get("num_tickets")
            if asked_tickets > max_amount:
                # add the error in the form
                form.errors["num_tickets"] = [
                    f"Pas assez de places disponibles pour acheter {asked_tickets} tickets. Il reste {max_amount} places."
                ]
                return render(
                    request,
                    "movies/buy_tickets.html",
                    {"form": form, "showing": showing, "max_amount": max_amount},
                )

            showing.tickets_sold += asked_tickets
            showing.save()
            return HttpResponseRedirect(reverse("movies:index"))
    else:
        form = BuyTicketsForm()
    return render(
        request,
        "movies/buy_tickets.html",
        {"form": form, "showing": showing, "max_amount": max_amount},
    )
    # return HttpResponse(f"Vous voulez acheter des billets pour la séance {showing}")
