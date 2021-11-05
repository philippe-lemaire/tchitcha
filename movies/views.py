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


def buy_tickets(request, showing_id):
    showing = get_object_or_404(Showing, pk=showing_id)
    max_amount = showing.room.capacity - showing.tickets_sold

    if request.method == "POST":
        # create the form and populate it
        form = BuyTicketsForm(request.POST)
        if form.is_valid():
            next = HttpResponseRedirect(reverse("movies:index"))
            if form.cleaned_data.get("num_tickets") > max_amount:
                return next
            showing.tickets_sold += form.cleaned_data.get("num_tickets")
            showing.save()
            return next
    else:
        form = BuyTicketsForm()
    return render(
        request,
        "movies/buy_tickets.html",
        {"form": form, "showing": showing, "max_amount": max_amount},
    )
    # return HttpResponse(f"Vous voulez acheter des billets pour la séance {showing}")
