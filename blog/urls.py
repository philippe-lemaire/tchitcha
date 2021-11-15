from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="detail",
    ),
    path("<int:year>/", views.ArticleYearArchiveView.as_view(), name="year_archive"),
    path(
        "<int:year>/<int:month>/",
        views.ArticleMonthArchiveView.as_view(month_format="%m"),
        name="month_archive",
    ),
    path("tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
    path("feed/", views.LatestEntriesFeed(), name="feed"),
]
