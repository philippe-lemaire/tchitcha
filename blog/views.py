from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Article, Tag

# Create your views here.
class IndexView(generic.ListView):
    def get_queryset(self):
        return (
            Article.objects.order_by("-pub_date")
            .filter(pub_date__lte=timezone.now())
            .filter(published=True)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class ArticleDetailView(generic.DetailView):
    model = Article


class ArticleYearArchiveView(generic.dates.YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = False


class ArticleMonthArchiveView(generic.dates.MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = False


class TagDetailView(generic.DetailView):
    model = Tag
