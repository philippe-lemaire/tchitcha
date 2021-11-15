from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.syndication.views import Feed
from markdownx.utils import markdownify

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

    paginate_by = 5


class ArticleDetailView(generic.DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["article_list"] = (
            Article.objects.order_by("-pub_date")
            .filter(pub_date__lte=timezone.now())
            .filter(published=True)
        )
        return context


class ArticleYearArchiveView(generic.dates.YearArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class ArticleMonthArchiveView(generic.dates.MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class TagDetailView(ArticleDetailView):
    model = Tag


class LatestEntriesFeed(Feed):
    title = "Les Actualités du Cinéma Tchitcha"
    link = "/feed/"
    description = (
        "Mis à jour avec les nouveaux articles où lors d’une modification du contenu."
    )

    def items(self):
        return Article.objects.order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdownify(item.content)

    # item_link is only needed if Article has no get_absolute_url method.
    def item_link(self, item):
        return reverse(
            "blog:detail",
            args=[
                item.pub_date.year,
                item.pub_date.month,
                item.pub_date.day,
                item.slug,
            ],
        )
